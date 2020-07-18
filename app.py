from functools import partial
import json
import os
import sys

from flask import Flask


current_path = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)


def _api_name(filename):
    return '/api/{}'.format(filename), filename


def _create_route(payload=None):
    return payload


for file in os.listdir(current_path):
    if file.endswith('.json'):
        try:
            with open(file) as json_file:
                payload = json.load(json_file)
                parsed_filename = file.split('.')[0]
                route, name = _api_name(parsed_filename)
                app.add_url_rule(
                    route, name, partial(_create_route, payload=payload))
        except:
            raise Exception(
                '{} has no values or is not using valid JSON format'.format(
                    file))


if __name__ == '__main__':
    port = 9001
    if len(sys.argv) > 1 and 'port' in sys.argv[1]:
        port = sys.argv[1].split('=')[1]
    app.run(port=port, debug=True)
