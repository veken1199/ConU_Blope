from flask import Flask,render_template, request
import pyodbc
app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":

        return Flask.redirect("/swipe", code=302)

    else:

        return render_template('login.html')


@app.route("/swipe")
def swipe():
    return render_template('swipe.html')

if __name__ == "__main__":
    app.run()