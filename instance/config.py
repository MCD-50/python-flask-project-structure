import os

# set debug to true for development
DEBUG = True

# App directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# App name
APP_NAME = "Python Flask Boilerplate"

# Threads per core
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "code"

# Secret key for signing cookies
SECRET_KEY = "code"

ALLOWED_HEADERS = ['Access-Token, X-Requested-With, Content-Type, Accept']
ALLOWED_ORIGINS = '*'
ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE']

# Environment - dev, stage, prod
APP_ENV = 'dev'

# Default values
PAGE_LIMIT = 20

# Error messages
ERROR = {
    'no_results': 'No results found',
    'permission': 'You do not have permission to do this action'
}

print(" * Loading config for " + APP_NAME)
