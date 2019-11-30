import os
from app import app, contollers


PORT = os.environ.get('PORT')


if __name__ == '__main__':
    # LOG.info('running environment: %s', os.environ.get('ENV'))
    app.config['DEBUG'] = os.environ.get('ENV') == 'development' # Debug mode if development env
    app.run(host='0.0.0.0', port=int(PORT)) # Run the app
