# Load environment variables
from dotenv import load_dotenv
load_dotenv()

from models import models
from utils import utils
from bottle import get, post, request, response

@post('/search')
def search():
    # Get json payload
    payload = request.json
    response.content_type = 'application/json'

    if(payload and 'criteria' in payload):
        # Transform to vector
        vector = utils.vectorize(payload['criteria'])
        videos = models.get_results_from_vector(vector)

        # Get responses from opensearch 
        return { 'error': False, 'message': 'Ok', 'results': videos}
    else:
        response.status = 400 # Bad request
        return { 'error': True, 'message': 'Search criteria must be provided' }
