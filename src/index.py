import os
from flask import Flask

app = Flask(__name__)

PORT = os.environ.get('PORT')

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    # LOG.info('running environment: %s', os.environ.get('ENV'))
    app.config['DEBUG'] = os.environ.get('ENV') == 'development' # Debug mode if development env
    app.run(host='0.0.0.0', port=int(PORT)) # Run the app
