from models import models
from bottle import get

@get('/ping')
def ping():
    return models.get_ping_response()
