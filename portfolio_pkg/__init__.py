from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect
from sassutils.wsgi import SassMiddleware

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = b'\xbf\xbc\xfaQ\xfc\x19W\x8aqo\xd6"\x8fo\xc4I'
    )
    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_mapping(test_config)
    
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    app.wsgi_app = SassMiddleware(app.wsgi_app, {
    __name__: ('static/sass', 'static/css', '/static/css')
    })
    
    # @app.route('/')
    # def index():
    #     return 'behold, a new structure'

    csrf = CSRFProtect()
    csrf.init_app(app)
    
    return app

app = create_app()

import portfolio_pkg.views