from __future__ import print_function
import io
from flask import Flask, request, Response
from PIL import Image

from predict import InferenceService

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/ping', methods=['GET'])
def ping():
    """
    Check server is up and running
    """

    try:

        return Response(response="pong", status=200, mimetype='text/plain')
    
    except Exception as e:

        return Response(response=e, status=500, mimetype='text/plain')

@app.route('/invocations', methods=['POST'])
def run_inference():
    """
    Run an inference
    """ 

    r = request

    # insert health checks, sanitation, etc. here
    if not r.data:
        return Response(response='image data required', status=400, mimetype='text/plain')
   
    try:
        
        # read image
        image = r.data
        image = Image.open(io.BytesIO(image))

        # run AI
        response, status = InferenceService.predict(image)     

    except Exception as e:

        response = json.dumps({"Server error": e})
        status=500
    
    return Response(response=response, status=status, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)