import sqlite3
import json

from pprint import pprint
## Connect to sqlite3 database
connection = sqlite3.connect("app.db", check_same_thread=False)
## Database cursor
cursor = connection.cursor()

orderby = "id"


cursor.execute("SELECT * FROM entries ORDER BY %s" % (orderby))
r = cursor.fetchall()

def make_dict(results):
    entries = {}
    entries[0] = {"orderby": orderby}
    i = 1
    for row in results:
        e = {}
        e["id"] = row[0]
        e["title"] = row[1]
        e["date"] = row[2]
        e["type"] = row[3]
        e["rating"] = row[4]
        e["image"] = row[5]
        e["description"] = row[6]
        entries[i] = e
        i += 1
    pprint(entries)


make_dict(r)

