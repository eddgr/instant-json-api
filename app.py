import sys

from instant_json_api import InstantJsonApi


if __name__ == '__main__':
    port = None
    if len(sys.argv) > 1 and 'port' in sys.argv[1]:
        port = sys.argv[1].split('=')[1]
    app = InstantJsonApi(port=port)
    app.run()
