from functools import partial
import json
import os
import sys

from flask import Flask
from flask_cors import CORS


current_path = os.path.dirname(os.path.abspath(__file__))


def _api_name(filename):
    return '/api/{}'.format(filename), filename


def _create_route(payload=None):
    return payload


class InstantJsonApi(object):
    def __init__(self, app=None, port=None):
        if app is None:
            app = Flask(__name__)
            CORS(app)
        if port is None:
            port = 9001
        self.app = app
        self.port = port
        self.init_app(app)
    
    def init_app(self, app):
        """
        Initialize the app to create routes for the JSON files.
        """
        for file in os.listdir(current_path):
            if file.endswith('.json'):
                try:
                    with open(file) as json_file:
                        payload = json.load(json_file)
                        parsed_filename = file.split('.')[0]
                        route, name = _api_name(parsed_filename)
                        app.add_url_rule(
                            route, name, partial(
                                _create_route, payload=payload))
                except:
                    raise Exception(
                        '{} has no values or is not using valid JSON format'.format(
                            file))

    def run(self):
        """
        Use for standalone run.
        """
        return self.app.run(port=self.port, debug=True)
        

if __name__ == '__main__':
    port = None
    if len(sys.argv) > 1 and 'port' in sys.argv[1]:
        port = sys.argv[1].split('=')[1]
    app = InstantJsonApi(port=port)
    app.run()
