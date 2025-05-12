from .config import Config
from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from .routes import init_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.wsgi_app = DispatcherMiddleware(
        app.wsgi_app,
        {'/metrics': make_wsgi_app()}
    )

    init_routes(app)
    return app
