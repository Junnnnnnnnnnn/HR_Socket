
from flask import Flask, Blueprint, render_template, request
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

@socket.on("connect")
def connect():
    userList.append(request.sid)
    print(userList)
    emit("connect", request.sid)

@socket.on("message")
def message(data):
    print("data", data)
    for user in userList:
        emit("message", data["sid"], to=user)

@socket.on("disconnect")
def disconnect():
    userList.remove(request.sid)

@socket.on("clickBox")
def clickBox(data):
    global clickBoxNum
    clickBoxNum = clickBoxNum + 1
    for user in userList:
        emit("clickBox", {"clickBoxNum": clickBoxNum,"box":data}, to=user)





