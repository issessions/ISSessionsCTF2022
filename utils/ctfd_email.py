#! /usr/bin/python3
import smtplib, ssl
import csv
import getpass
import textwrap
import traceback
from termcolor import colored

port = 465
email = ""
password = getpass.getpass()
context = ssl.create_default_context()

data = []
# team_id | username |  password | player | email
with open("team_password.csv") as input:
    r = csv.DictReader(input)
    for line in r:
        data.append(line)
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)
    for p in data:
        message = textwrap.dedent(
            f"""\
            From: {email}
            To: {p["email"]}
            Subject: ISSessions 2022 CTF Kibana Credentials

            Hello {p["player"]},

            Here are your team's login credentials for the kibana challenges:

            Username: {p["username"]}
            Password: {p["password"]}

            You will be given a url during the event.
            """
        )
        try:
            print(f"Sending email to {p['player']}({p['email']}) ", end="")
            server.sendmail(email, p["email"], message)
            print(colored("[OK]", "green"))
        except:
            traceback.format_exc()
