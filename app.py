

from flask import Flask
from .route import register_route


def create_app():
    app = Flask(__name__)
    register_route(app)
    return app



if __name__ == '__main__':
    app = create_app()
    app.run(port=8000)