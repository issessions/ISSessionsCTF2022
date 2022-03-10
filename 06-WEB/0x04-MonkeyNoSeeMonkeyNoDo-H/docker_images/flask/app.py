import sqlite3
import json
from helper import *
from flask import Flask, request

## Flask app
app = Flask(__name__)
app.secret_key = "blindsql"
## Connect to sqlite3 database
connection = sqlite3.connect("app.db", check_same_thread=False)
## Database cursor
cursor = connection.cursor()

@app.route("/", methods=["GET", "POST"], defaults={"orderBy": "date"})
def index(orderBy):

    if request.data != b"":
        req = request.data.decode(encoding="utf-8")[8:]
        orderBy = req

    try:
        ## Challenge #2 - Blind SQL injection
        cursor.execute("SELECT * FROM entries ORDER BY %s" % (orderBy))
        results = cursor.fetchall()
        response = app.response_class(
            response = json.dumps(make_dictionary(results, orderBy)),
            status = 200,
            mimetype = "application/json"
        )

        response.headers["Flag"] = "monkeyCTF{just_kidding}"
        return response
    except Exception as ex:
        ## BAD!
        pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)