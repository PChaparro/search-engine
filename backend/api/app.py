from bottle import run

# Setup routes
from controllers import controllers

run(host="localhost", port=8080, debug=True, reloader=True)
