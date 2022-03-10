#! /usr/bin/python3
from curses.ascii import SP
import requests
import random
import string
import mysql.connector
import csv
from termcolor import colored
import pprint


def main():
    p = pprint.PrettyPrinter(indent=4).pprint
    kibana = ""
    es = ""
    api_key = ""
    s = Space(kibana, api_key)
    r = Role(kibana, api_key)
    u = User(es, api_key)
    o = SavedObject(kibana, api_key)

    with mysql.connector.connect(
        host="mariadb.ctfd.svc.cluster.local",
        user="ctfd",
        password="ctfd",
        database="ctfd",
    ) as conn, conn.cursor(dictionary=True) as cursor:
        get_teams = "select id, name from teams"
        cursor.execute(get_teams)
        teams = cursor.fetchall()

        # create spaces and get passwords
        for t in teams:
            t["name"] = cleanName(t["name"])
            name = t["name"]
            result = create(name, s, o, r, u)
            if result:
                t["password"] = result

        with open("team_password.csv", "w") as file:
            w = csv.DictWriter(
                file, fieldnames=["id", "username", "password", "player", "email"]
            )
            w.writeheader()
            for t in teams:
                # do sql to get list of users on a team
                get_players = (
                    f"select team_id, name, email from users where team_id={t['id']}"
                )
                cursor.execute(get_players)
                players = cursor.fetchall()
                for p in players:
                    # team_id | username |  password | player | email
                    row = {}
                    row["id"] = t["id"]
                    row["email"] = p["email"]
                    row["username"] = t["name"]
                    row["password"] = t["password"]
                    row["player"] = p["name"]
                    w.writerow(row)
    # print()
    # input("Press enter to delete")
    # # delete the things
    # for t in teams:
    #     t["name"] = cleanName(t["name"])
    #     name = t["name"]
    #     delete(name, s, r, u)


def create(name, s, o, r, u):
    print("------------------------")
    print(colored(name, "yellow"))
    # create space
    print(f"Creating Space ", end="")
    result = s.createSpace(name)
    print(isSuccess(result, 200))

    # set space config
    print(f"Setting Space Config ", end="")
    result = o.createSavedObject("config", "7.17.0", name)
    print(isSuccess(result, 200))

    # copy index
    print(f"Copying Index Config ", end="")
    result = s.copySavedObjects(name)
    print(isSuccess(result, 200))

    # create role
    print(f"Creating Role ", end="")
    result = r.createRole(name)
    print(isSuccess(result, 204))

    # create user
    print(f"Creating User ", end="")
    result = u.createUser(name, [name])
    text = (
        colored("[SUCCESSFUL]", "green")
        if result["created"] == True
        else colored("[UNSUCESSFUL]", "red")
    )
    print(text)
    return result.get("password")


def delete(name, s, r, u):
    print("------------------------")
    print(colored(name, "yellow"))
    # delete user
    print(f"Deleting User ", end="")
    result = u.deleteUser(name)
    print(isSuccess(result, 200))

    # delete role
    print(f"Deleting Role ", end="")
    result = r.deleteRole(name)
    print(isSuccess(result, 204))

    # delete space
    print(f"Deleting Space ", end="")
    result = s.deleteSpace(name)
    print(isSuccess(result, 204))
    return None


def cleanName(name):
    # make lowercase
    name = name.lower()
    # convert symbols
    safe = "-_"
    symbols = string.punctuation.translate({ord(i): None for i in safe})
    name = name.translate({ord(i): None for i in symbols})
    # convert whitespace
    name = name.translate({ord(i): ord("_") for i in string.whitespace})
    return name


def isSuccess(result, success):
    text = (
        colored("[SUCCESSFUL]", "green")
        if result.status_code == success
        else result.json()
    )
    return text


class Api:
    def __init__(self, url, api_key):
        self.headers = {
            "Authorization": f"ApiKey {api_key}",
            "kbn-xsrf": "true",
            "content-type": "application/json;charset=UTF-8",
        }
        self.domain = url


class Search(Api):
    def __init__(self, es_url, api_key):
        super().__init__(es_url, api_key)

    def search(self):
        url = f"{self.domain}/logs-*-default/_search"
        payload = {
            "q": "@timestamp:[* TO 2020-09-24T11:39:00.000Z]",
        }
        return requests.get(url, headers=self.headers, data=payload).json()

    def delete(self):
        url = f"{self.domain}/logs-*-default/_delete_by_query"
        payload = {
            "query": {
                "range": {
                    "@timestamp": {
                        "lte": "2022-02-24T00:00:00.000Z",
                    }
                }
            },
            "sort": [{"@timestamp": {"order": "asc"}}],
            "fields": [{"field": "@timestamp"}],
            # "track_total_hits": 1,
            "_source": False,
        }
        return requests.post(url, headers=self.headers, json=payload).json()


class Space(Api):
    def __init__(self, kibana_url, api_key):
        super().__init__(kibana_url, api_key)

    def getSpaces(self):
        url = f"{self.domain}/api/spaces/space"
        return requests.get(url, headers=self.headers).json()

    def getSpace(self, name):
        url = f"{self.domain}/api/spaces/space/{name}"
        return requests.get(url, headers=self.headers).json()

    def createSpace(self, name):
        url = f"{self.domain}/api/spaces/space"
        data = {"name": name, "id": name, "disabledFeatures": ["enterpriseSearch"]}
        return requests.post(url, headers=self.headers, json=data)

    def deleteSpace(self, name):
        url = f"{self.domain}/api/spaces/space/{name}"
        return requests.delete(url, headers=self.headers)

    def copySavedObjects(self, spaces):
        url = f"{self.domain}/api/spaces/_copy_saved_objects"
        data = {
            "objects": [
                {"type": "index-pattern", "id": "logs-*"},
            ],
            "spaces": [spaces],
            "createNewCopies": "false",
            "overwrite": "true",
        }
        return requests.post(url, headers=self.headers, json=data)

    def getFeatures(self):
        url = f"{self.domain}/api/features"
        return requests.get(url, headers=self.headers, json=True).json()


class User(Api):
    def __init__(self, es_url, api_key):
        super().__init__(es_url, api_key)

    def getUsers(self):
        url = f"{self.domain}/_security/user"
        return requests.get(url, headers=self.headers).json()

    def __randomPassword(self, length=16):
        characters = string.ascii_letters + string.digits
        ambiguous = "0oOil1"
        characters = characters.translate({ord(i): None for i in ambiguous})
        return "".join(random.choice(characters) for i in range(length))

    def createUser(self, username, roles, pw_length=16):
        url = f"{self.domain}/_security/user/{requests.utils.quote(username)}"
        data = {
            "password": self.__randomPassword(pw_length),
            "roles": roles,
        }
        status = requests.post(url, headers=self.headers, json=data).json()
        status["password"] = data["password"]
        return status

    def deleteUser(self, username):
        url = f"{self.domain}/_security/user/{username}"
        return requests.delete(url, headers=self.headers)

    def updateUser(self, username, roles=[]):
        url = f"{self.domain}/_security/user/{username}"
        if roles:
            data = {
                "roles": roles,
            }
        return requests.put(url, headers=self.headers, json=data).json()


class Role(Api):
    def __init__(self, kibana_url, api_key):
        super().__init__(kibana_url, api_key)

    def getRole(self, name):
        url = f"{self.domain}/api/security/role/{name}"
        return requests.get(url, headers=self.headers).json()

    def createRole(self, name):
        url = f"{self.domain}/api/security/role/{name}"
        data = {
            "elasticsearch": {
                "indices": [
                    {
                        "allow_restricted_indices": False,
                        "names": ["logs-*-default"],
                        "privileges": ["read"],
                    }
                ]
            },
            "kibana": [
                {
                    "feature": {"discover": ["read"]},
                    "spaces": [f"{name}"],
                }
            ],
        }
        return requests.put(url, headers=self.headers, json=data)

    def deleteRole(self, name):
        url = f"{self.domain}/api/security/role/{name}"
        return requests.delete(url, headers=self.headers)


class SavedObject(Api):
    def __init__(self, kibana_url, api_key):
        super().__init__(kibana_url, api_key)

    def findSavedObjects(self, type, space_id="default", search=""):
        url = f"{self.domain}/s/{space_id}/api/saved_objects/_find"
        params = {"type": type, "search": search}
        return requests.get(url, headers=self.headers, params=params).json()

    def updateSavedObject(self, type, id, space_id="default"):
        url = f"{self.domain}/s/{space_id}/api/saved_objects/{type}/{id}"
        data = {
            "attributes": {
                "defaultIndex": "logs-*",
                "defaultRoute": "/app/discover",
                "search:queryLanguage": "lucene",
                "theme:darkMode": True,
            }
        }
        return requests.put(url, headers=self.headers, json=data).json()

    def createSavedObject(self, type, id, space_id="default"):
        url = f"{self.domain}/s/{space_id}/api/saved_objects/{type}/{id}"
        data = {
            "attributes": {
                "defaultIndex": "logs-*",
                "defaultRoute": "/app/discover",
                "search:queryLanguage": "lucene",
                "theme:darkMode": True,
            }
        }
        return requests.post(url, headers=self.headers, json=data)


if __name__ == "__main__":
    main()
