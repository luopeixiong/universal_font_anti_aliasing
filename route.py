

import flask
from flask import request, jsonify
from .universal_font_anti_aliasing.anti_aliasing import anti


def register_route(app:flask.Flask):
    @app.route("/ocr", methods=["POST"])
    def ocr():
        font_url = request.form["font_url"]
        words = request.form["words"]
        try:
            result = anti(font_url, words)
            return jsonify(
                {
                    "font_url": font_url,
                    "words": words,
                    "result": result.decode("utf-8"),
                }
            )
        except Exception as e:
            return jsonify(
                {
                    "error": str(e),
                }
            )

