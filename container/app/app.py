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
    health = InferenceService.get_model() is not None  
    
    # choose a response
    if health:
        response = "loaded model successfully!"
        status = 200
    else:
        response = "model not loaded"
        status = 500

    return flask.Response(response=response, status=status, mimetype='text/plain')

@app.route('/predict', methods=['POST'])
def run_inference():
    """
    Run an inference
    """ 
    
    # You can insert more robust checks here
    if not flask.request.files.get("image"):
        return flask.Response(response='image required in request', status=400, mimetype='text/plain')

    # read the image in PIL format
    image = flask.request.files["image"].read()
    image = Image.open(io.BytesIO(image))

    response = InferenceService.predict(image)

    # run AI
    try:
        response = InferenceService.predict(image)
        status = 200
    except:
        response = json.dumps('server error')
        status = 500
         
    return flask.Response(response=response, status=status, mimetype='application/json')

# some minimal UX
@app.route("/", methods=["GET"])
def home():
    """
    home page message
    """
    return "Hello, POST your image to '/predict' to get this AI brain working.. "

# some more minimal UX
@app.route("/predict", methods=["GET"])
def reminder_to_POST():
    """
    predict page message
    """
    return "Hi, if you POST me an image I'll try and figure out what it is.."