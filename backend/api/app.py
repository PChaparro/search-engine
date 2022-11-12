from bottle import run, hook, response

_allow_origin = "*"
_allow_methods = "GET, POST, OPTIONS"
_allow_headers = "Origin, Accept, Content-Type, X-Requested-With"

# Setup routes
from controllers import controllers

# Allow cors
@hook("after_request")
def enable_cors():
    response.headers["Access-Control-Allow-Origin"] = _allow_origin
    response.headers["Access-Control-Allow-Methods"] = _allow_methods
    response.headers["Access-Control-Allow-Headers"] = _allow_headers


run(host="localhost", port=8080, debug=True, reloader=True)
