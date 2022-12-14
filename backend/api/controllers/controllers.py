# Load environment variables
from dotenv import load_dotenv

load_dotenv()

from models import models
from utils import utils
from bottle import get, post, request, response


@post("/search")
def search():
    # Get json payload
    payload = request.json
    response.content_type = "application/json"

    if payload and "criteria" in payload:  # Provided criteria

        if payload["criteria"].strip() == "":  # Non empty criteria
            response.status = 400  # Bad request
            return {"error": True, "message": "Search criteria must not be empty"}

        # Transform to vector
        vector = utils.vectorize(payload["criteria"])
        # Search on opensearch
        videos = models.get_results_from_vector(vector)

        # Send response
        return {"error": False, "message": "Ok", "results": videos}
    else:
        response.status = 400  # Bad request
        return {"error": True, "message": "Search criteria must be provided"}


@get("/random")
def random():
    # Get random videos from open search
    videos = models.get_random_videos()
    return {"error": False, "message": "Ok", "results": videos}
