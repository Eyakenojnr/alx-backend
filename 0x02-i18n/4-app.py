#!/usr/bin/env python3
"""
Force a particular locale by passing `locale=fr` parameter to app URLs
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """
    Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select and return language match based on supported languages
    """
    loc = request.args.get("locale")
    if loc in app.config["LANGUAGES"]:
        return loc
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/', strict_slashes=False)
def get_index() -> str:
    """
    Home/index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
