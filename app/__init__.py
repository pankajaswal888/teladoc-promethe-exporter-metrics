# Import configuration
from .config import Config

# Import Flask & related web framework components
from flask import Flask

# Import Prometheus metrics
from prometheus_client import make_wsgi_app

# Import middleware to handling multiple WSGI applications
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Import route initialization func
from .routes import init_routes

def create_app(config_class=Config):
    
    app = Flask(__name__)
    
    # Load configuration from the specified class
    app.config.from_object(config_class)

    # Set up WSGI middleware to handle both of them:
    # - Regular Flask routes (app.wsgi_app)
    # - Prometheus metrics endpoint ('/metrics')
    
    app.wsgi_app = DispatcherMiddleware(
        app.wsgi_app,
        {'/metrics': make_wsgi_app()} # Prometheus metrics endpoint
    )

    init_routes(app)
    return app
