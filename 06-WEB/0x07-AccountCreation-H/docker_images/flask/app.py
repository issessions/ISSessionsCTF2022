import sqlite3
import os
from functools import wraps
from flask import Flask, render_template, request, flash, redirect, session, make_response, jsonify, Response

## Flask app
app = Flask(__name__)
app.secret_key = 'secret'
## Connect to sqlite3 database
connection = sqlite3.connect("app.db", check_same_thread=False)
## Database cursor
cursor = connection.cursor()

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect("/login")
    return wrap

## Main page
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    try:
        cursor.execute("SELECT * FROM bananas")
        b = cursor.fetchall()
    except:
        pass
    if request.method == "GET":
        return render_template("index.html", b=b, size=len(b))

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/login")

## SecureAuth Challenge
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        ## Check if username and password are empty
        if not request.form.get("username") or not request.form.get("password"):
            flash("Please enter username and password.", "danger")
            return render_template("login.html")
        ## Get username and password values from request
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            ## SELECT query to get user
            sqlQuery="""SELECT username FROM users WHERE username = (?) and password =(?)"""
            tuple1 = (username,password)
            cursor.execute(sqlQuery,tuple1)
            ## Get result
            result = cursor.fetchone()
            ## User not found
            if result == None:
                flash("User not found.", "danger")
                return render_template("login.html")
            else:
                cursor.execute("SELECT privilege FROM users WHERE username = '%s' AND password = '%s'" % (username, password))
                result = cursor.fetchone()
                res = int(result[0])
                print(res)
                if(res!=1):
                    flash("monkeyCTF{account_creation_injection}")
                session["logged_in"] = True
                return redirect("/")
        except Exception as e:
            print("problem:" + str(e))
            flash("An unexpected error occured, please try again.\n", "danger")
            return render_template("login.html")
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        if not request.form.get("username") or not request.form.get("password"):
            flash("Please enter username and password.", "danger")
            return render_template("login.html")
        username = request.form.get("username")
        password = request.form.get("password")
        cursor.execute("INSERT into users (username,password,privilege) VALUES('%s','%s','%d')"%(username,password,1))

        connection.commit()
        return render_template("login.html")

if __name__ == "__main__":
    ## Run in debug mode
    app.run(host="0.0.0.0", port=5000)