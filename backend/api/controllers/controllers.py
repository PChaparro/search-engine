from models import models
from utils import utils
from bottle import get, post, request, response

@post('/search')
def search():
    # Get json payload
    payload = request.json
    response.content_type = 'application/json'

    if(payload and 'criteria' in payload):
        vector = utils.vectorize(payload['criteria'])
        return { 'error': False, 'message': 'Ok', 'vector': list(vector)}
    else:
        response.status = 400 # Bad request
        return { 'error': True, 'message': 'Search criteria must be provided' }
