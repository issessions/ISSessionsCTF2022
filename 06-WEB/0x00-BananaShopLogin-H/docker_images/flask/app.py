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
    else:
        """
        
        TODO: REVIEW
        
        
        """
        alert = request.get_json()["alert"]
        print(type(alert))
        if alert == True:
            print("re")
            flash("flag")
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
        username = request.form.get("username").replace(" ", "")
        password = request.form.get("password").replace(" ", "")
        try:
            ## SELECT query to get user
            cursor.execute("SELECT username FROM users WHERE username = '%s' AND password = '%s'" % (username, password))
            ## Get result
            result = cursor.fetchone()[0]
            ## User not found
            if result == 0:
                flash("User not found.", "danger")
                return render_template("login.html")
            else:
                session["logged_in"] = True
                if username[:5].lower() == "admin":
                    flash("monkeyCTF{ba5ic_5q1_inj3cti0n5}", "warning")
                    return redirect("/")
                elif username == "OTHER": ## CHANGE THIS 
                    pass
                else:
                    flash("Logged in successfully.", "warning")
                    return redirect("/login")
        except Exception as e:
            print("problem:" + str(e))
            flash("An unexpected error occured, please try again.\n", "danger")
            return render_template("login.html")
        return render_template("login.html")

@app.route("/banana")
@login_required
def banana():
    try:
        id = request.args["id"]
        ## Vulnerable query
        cursor.execute("SELECT * FROM bananas WHERE id = '%s'" % (id))
        b = cursor.fetchall()
    except:
        pass
    return render_template("banana.html", b=b, size=len(b))

@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    if request.method == "GET":
        response = make_response(render_template("checkout.html"))
        response.set_cookie("flag", "", expires=0)
        return response
    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        address = request.form.get("address").replace("script", "")
        city = request.form.get("city")
        province = request.form.get("province")
        postal = request.form.get("postal")
        ## Write email to file
        with open("emails.txt", "a") as f:
            f.write(email + "\n")
        ## List of user attributes
        user = [fname, lname, email, address, city, province, postal]
        return render_template("confirmation.html", u=user)
        
@app.route("/confirmation", methods=["POST"])
@login_required
def confirmation():
    req = request.get_json()
    if req == "True":
        print(req.upper())
        flash("monkeyCTF{x55_c0u1d_b3_much_m0r3_dang3r0u5}", "warning")
        response = make_response(jsonify({}), 200)
        return response

@app.route("/emails")
@login_required
def emails():
    file = request.args.get("file")
    ## No filename from request
    if not file:
        file = "emails.txt"
    try:
        ## Path name
        path = (os.getcwd() + "/" + file).replace("../", "")
        ## Set path to default path if filename is one in app directory
        if file in os.listdir("."):
            path = "emails.txt"
        content = "PATH: " + path + "\n-----\n"
        ## Read file and saves content into variable
        with open(path, "r") as f:
            content += f.read()
        return Response(content, mimetype='text/plain')
    except IOError:
        with open("emails.txt", "r") as f:
            content += f.read()
        return Response(content, mimetype='text/plain')

if __name__ == "__main__":
    ## Run in debug mode
    app.run(host="0.0.0.0", port=5000)