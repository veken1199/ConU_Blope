from flask import Flask, render_template, request
from tinydb import TinyDB, Query
import pypyodbc, json

app = Flask(__name__)

db = TinyDB('db.json')
command = Query()
UserId = " "
Name = " "
GPA = 0.0
School = " "
Year = 0
Program = " "
Picture = " "


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == 'POST'
        data = request.data
        userData = json.loads(data.decode("utf-8"))
        for key, value in dict.items(userData["uid"]):
            UserId = str(value)
        for key, value in dict.items(userData["School"]):
            School = str(value)
        for key, value in dict.items(userData["Program"]):
            Program = str(value)
        for key, value in dict.items(userData["Picture"]):
            Picture = str(value)
        for key, value in dict.items(userData["Name"]):
            Name = str(value)
        login(UserId, School, Program, Picture, Name)
    elif request.method == 'GET':
        return render_template('login.html')


def login(UserId, School, Program, Picture, Name):
    if not db.search(command['UserId'] == UserId):
        db.insert({'UserId': UserId, 'School': School, 'Program': Program, 'Picture': Picture, 'Name': Name})
        # if user exist extract school and gpa from table
    else:
        db.update({'School': School}, command['UserId'] == UserId)
        db.update({'Program': Program}, command['UserId'] == UserId)


@app.route("/swipe", methods=['GET', 'POST'])
def update():
    return "hello world"


def checkForMatch():
    potentialMatch = db.search(command['School'] == School, command['Program'] == Program)


if __name__ == "__main__":
    app.run()