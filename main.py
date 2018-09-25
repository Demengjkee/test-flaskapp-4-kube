#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import abort
import json
import time
import logging


ERROR_RESP = False
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def init():
    for i in range(5):
        logger.info("Starting app atempt {}".format(i+1))
        time.sleep(5)
    return Flask(__name__)

app = init()

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
