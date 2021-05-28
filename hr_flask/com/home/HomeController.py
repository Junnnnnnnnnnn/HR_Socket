from flask import Flask, Blueprint, render_template, request, json
from flask_restx import Api, Namespace, Resource
from flask_socketio import emit

from hr_flask import socket

bp = Blueprint("HomeController", __name__)
ns = Namespace(name="", description="HR SOCKET")
api = Api(
    bp,
    title="HR SOCKET",
    version="1.0.0",
    doc="/api/docs",
    description="socket",
    license="yotdark soft"
)


userList = []
clickBoxNum = 0
@ns.route("/")
class index(Resource):
    @ns.doc(params={"id": "아이디"})
    def get(self):
        """
            테스트 로그인
        """

@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():

    return render_template("index.html")

@bp.route("/test", methods=["GET"])
def test():

    return render_template("socket/sockTest.html")


