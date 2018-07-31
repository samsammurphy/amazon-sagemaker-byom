from __future__ import print_function
import os
import json
import flask
from PIL import Image
import io

from predict import InferenceService

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/ping', methods=['GET'])
def ping():
    """
    Determine if the container is healthy.
    """

    # You can insert a health check here
    return flask.Response(response="pong", status=200, mimetype='text/plain')

@app.route('/invocations', methods=['POST'])
def run_inference():
    """
    Run an inference
    """ 
    
    # insert health checks and sanitation here
    if not flask.request.files.get("image"):
        return flask.Response(response='image required in request', status=400, mimetype='text/plain')

    # read the image
    image = flask.request.files["image"].read()
    image = Image.open(io.BytesIO(image))

    # run AI
    response, status = InferenceService.predict(image)        
    return flask.Response(response=response, status=status, mimetype='application/json')

# some minimal UX
@app.route("/", methods=["GET"])
def home():
    """
    home page message
    """
    return "Hello, POST your image to '/invocations' to get this AI brain working.. "

# some more minimal UX
@app.route("/invocations", methods=["GET"])
def reminder_to_POST():
    """
    invocations message
    """
    return "Hi, if you POST me an image I'll try and figure out what it is.."