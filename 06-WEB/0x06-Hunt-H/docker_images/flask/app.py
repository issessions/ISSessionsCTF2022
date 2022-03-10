from urllib import response
from flask import Flask, make_response, render_template, Response

app = Flask(__name__)

"""
robots.txt
CSS
JS
HTML
Cookie
"""

@app.route("/")
def index():
    response = make_response(render_template("index.html"))
    response.set_cookie("FLAG-PART-4", "hunt_")
    return response

@app.route("/robots.txt")
def noindex():
    resp = Response(response="User-Agent: *\nDisallow: /\n\nFLAG-PART-5: good_job}", status=200, mimetype="text/plain")
    resp.headers["Content-Type"] = "text/plain; charset=utf-8"
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)