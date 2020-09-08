
import os
import sys

sys.path.append(os.path.dirname(__file__))

from flask import Flask
from route import register_route


def create_app():
    app = Flask(__name__)
    register_route(app)
    return app



if __name__ == '__main__':
    app = create_app()
    app.run(port=8000)