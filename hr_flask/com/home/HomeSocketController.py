from flask import Flask, Blueprint, render_template, request, json
from flask_restx import Api, Namespace, Resource
from flask_socketio import emit
from hr_flask import socket

bp = Blueprint("HomeSocketController", __name__,url_prefix="/socket");

userList = []

@bp.route("/main")
def main():
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
    print("clickBoxNum ::: ", clickBoxNum)
    socket.emit("clickBox", {"clickBoxNum": clickBoxNum, "box": data})