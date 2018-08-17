"""
Local REST requests for server testing

"""

import os
import json
import requests


def get(url):

    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return response.status_code

def post(filepath, route=None, mime='image/jpeg', port='8080'):

    try:

        
        img = open(filepath, 'rb').read()

        url = os.path.join('http://localhost:'+port, route) 
        
        # we will need to let the server know what kind of file it is
        headers = {'content-type': mime} 
        
        # POST it to the endpoint and listen for response from server
        response = requests.post(url, data=img, headers=headers) 
        
        if response.status_code == 200:
            return json.loads(response.text)

    except Exception as e:

        return e
