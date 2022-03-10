from flask import Flask, make_response, render_template, request


app = Flask(__name__)

@app.route("/")
def index():

    cookie = request.cookies.get("user")

    if cookie == "e25hbWU6ICJzdXBlcmNvb2tpZSIsIGNvb2w6ICJUcnVlIn0=":
        resp = make_response(render_template("admin.html", flag="monkeyCTF{c00kie_monster}"))
    else:
        resp = make_response(render_template("index.html", cookie="cookie " * 124))
        resp.set_cookie("user", "e25hbWU6ICJub3JtYWxfdXNlciIsIGNvb2w6ICJGYWxzZSJ9")

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)