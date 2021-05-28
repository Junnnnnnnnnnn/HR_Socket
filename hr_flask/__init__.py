import os

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

socket = SocketIO()
def create_app():
    app = Flask(__name__, static_folder="static", template_folder="views")

    app.secret_key = os.urandom(16)
    app.secret_key = "YOTDARK_SECRET_KEY"
    CORS(app, resources={r"*": {"origins": "*"}})

    from hr_flask.com.home import HomeController
    app.register_blueprint(HomeController.bp)
    HomeController.api.add_namespace(HomeController.ns)
    from hr_flask.com.test import TestController
    app.register_blueprint(TestController.bp)
    from hr_flask.com.home import HomeSocketController
    app.register_blueprint(HomeSocketController.bp)
    socket.init_app(app)

    return app