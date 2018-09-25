#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import abort
import json

app = Flask(__name__)
ERROR_RESP = False

@app.route("/", methods=['GET'])
def index():
    global ERROR_RESP
    if not ERROR_RESP:
        return make_response(render_template("index.html", name="index"), 200)
    else:
        abort(403)

@app.route("/change_resp", methods=['POST'])
def chenge_resp():
    global ERROR_RESP
    ERROR_RESP = not ERROR_RESP
    return make_response(json.dumps({"result": "ok"}))

if __name__ == "__main__":
    app.run()
