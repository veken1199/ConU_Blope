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
def index():
    if request.method == 'POST':

        Name = request.form['username']
        School =request.form['school']
        Program = request.form['program']
        Picture = request.form['pic']
        UserId = request.form['uid']

        print(Name)

        login(UserId, School, Program, Picture, Name)
        return render_template('swipe.html')

    if request.method == 'GET':
        return render_template('login.html')


def login(UserId, School, Program, Picture, Name):
    if not db.search(command['UserId'] == UserId):
        db.insert({'UserId': UserId, 'School': School, 'Program': Program, 'Picture': Picture, 'Name': Name})
        # if user exist extract school and gpa from table
    else:
        db.update({'School': School}, command['UserId'] == UserId)
        db.update({'Program': Program}, command['UserId'] == UserId)

    return render_template("swipe.html")


@app.route("/swipe", methods=['GET', 'POST'])
def update():
    return render_template('swipe.html')


def checkForMatch():
    potentialMatch = db.search(command['School'] == School, command['Program'] == Program)


if __name__ == "__main__":
    app.run()