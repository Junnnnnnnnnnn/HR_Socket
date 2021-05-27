import os

from flask import Flask
from flask_socketio import SocketIO

socket = SocketIO()
def create_app():
    app = Flask(__name__, static_folder="static", template_folder="views")

    app.secret_key = os.urandom(16)
    app.secret_key = "YOTDARK_SECRET_KEY"

    from hr_flask.com.home import HomeController
    app.register_blueprint(HomeController.bp)
    HomeController.api.add_namespace(HomeController.ns)

    socket.init_app(app)


    return app