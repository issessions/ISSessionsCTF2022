#!/usr/bin/python3
import requests
import sys
import os
import argparse
from typing import List, Dict


class Challenge:
    # Special header for Github Project's API
    HEADER: Dict = {"Accept": "application/vnd.github.inertia-preview+json"}
    # Status of card checkboxes
    box_status = False
    # Default CTF challenge categories
    CATEGORIES: Dict = {
        "TESTING": "TESTING",
        "WELCOME": "00-WELCOME",
        "PROGRAMMING": "01-PROGRAMMING",
        "REVERSING": "02-REVERSING",
        "FORENSICS": "03-FORENSICS",
        "CRYPTOGRAPHY": "04-CRYPTOGRAPHY",
        "NETWORK": "05-NETWORK",
        "WEB": "06-WEB",
        "PWN": "07-PWN",
        "STORYMODE": "08-STORYMODE",
        "MISC": "09-MISC",
    }

    def __init__(self, category: str, name: str) -> None:
        self.challenge_category = category
        self.challenge_name = name

        try:
            repo = os.environ.get("REPO")
            repo = repo.split("/")

            # Auth information (USERNAME, Github-Personal-Access-Token)
            self._AUTH = (repo[0], os.environ["GITHUB_TOKEN"])

            # API URL to the repository
            self.REPO_API_URL: str = (
                f"https://api.github.com/repos/{repo[0]}/{repo[1]}/projects"
            )
        except KeyError as e:
            print(f"ERROR: Missing {e} environment variable.")
            sys.exit(1)

    def get_columns(self) -> List:
        """
        Returns the columns from a project
        """
        # URL to access columns in the repository's Github Projects
        columns_url = requests.get(
            self.REPO_API_URL, auth=self._AUTH, headers=self.HEADER
        ).json()[0]["columns_url"]

        # List of columns in the repository's Github Projects
        columns = requests.get(columns_url, auth=self._AUTH, headers=self.HEADER).json()

        # verify that all columns exist
        added_column = False
        column_names = [name["name"] for name in columns]
        for cat in self.CATEGORIES.values():
            if cat not in column_names:
                # create the cat column
                added_column = True
                requests.post(
                    columns_url,
                    json={"name": cat},
                    auth=self._AUTH,
                    headers=self.HEADER,
                )

        # if a column was added, then get the list again
        if added_column:
            columns = requests.get(columns_url, auth=self._AUTH, headers=self.HEADER).json()

        # Return list of columns
        return columns

    def get_card(self) -> str:
        """
        Return a card template
        """
        url = f"https://github.com/{os.environ['REPO']}/tree/{os.environ.get('BRANCH').split('/')[-1]}"
        return f"[{self.CATEGORIES.get(str(self.challenge_category))[0:2]}-{self.challenge_name}]({url})\
                    \n- [{'x' if self.box_status == True else ' '}] ✅ Done\
                    \n---\
                    \nDifficulty: "

    def create(self) -> None:
        """
        Create a card in challenge_category column
        """
        # Find the appropriate column and create card
        for column in self.get_columns():
            # Check if category matches
            if column["name"] == self.CATEGORIES.get(str(self.challenge_category)):
                # Post the card
                requests.post(
                    column["cards_url"],
                    json={"note": self.get_card()},
                    auth=self._AUTH,
                    headers=self.HEADER,
                )
                break

    def move(self, op: int) -> None:
        """
        Move from challenge_category column to TESTINGS column
        """
        card_note = None

        if op == 0:
            option = [self.CATEGORIES.get(str(self.challenge_category)), "TESTING"]
        elif op == 1:
            option = ["TESTING", self.CATEGORIES.get(str(self.challenge_category))]
            self.box_status = True
            
        # Look through the columns list to find appropriate category
        for column in self.get_columns():
            # Check if category matches
            if column["name"] == option[0]:
                # Look through each card in the column
                for card in requests.get(
                    column["cards_url"], auth=self._AUTH, headers=self.HEADER
                ).json():
                    # Check if card name matches
                    if (
                        f"{self.CATEGORIES.get(str(self.challenge_category))[0:2]}-{self.challenge_name}"
                        in card["note"]
                    ):
                        # Store card content
                        card_note = card["note"]

                        # Remove card from column
                        requests.delete(
                            card["url"], auth=self._AUTH, headers=self.HEADER
                        )
                        break

        # Recreate the card in column
        for column in self.get_columns():
            if column["name"] == option[1]:
                requests.post(
                    column["cards_url"],
                    json={"note": self.get_card()},
                    auth=self._AUTH,
                    headers=self.HEADER,
                )
                break


def main():
    # Command line argument parser
    parser = argparse.ArgumentParser()
    op = parser.add_mutually_exclusive_group(required=True)
    op.add_argument(
        "--create", action="store_true", help="creating a branch and a card"
    )
    op.add_argument("--pull-request", action="store_true", help="testing a challenge")
    op.add_argument(
        "--merged", action="store_true", help="finished testing challenge and merged"
    )
    args = parser.parse_args()

    # Get branch name
    branch = os.environ.get("BRANCH")
    branch = branch.split("/")[-1]
    branch = branch.split("-")

    c = Challenge(branch[0].upper(), "-".join(branch[1:]))

    # Handle arguments
    if args.create:
        c.create()
    elif args.pull_request:
        c.move(0)
    elif args.merged:
        c.move(1)


if __name__ == "__main__":
    main()
