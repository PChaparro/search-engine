# Load environment variables
from dotenv import load_dotenv
from bottle import run
load_dotenv()

# Setup routes
from controllers import controllers
controllers.search()

run(host='localhost', port=8080, debug=True, reloader=True)
