from flask import Flask,render_template, request,url_for
import pypyodbc
app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        return"lk"

    else:
        return render_template('login.html')


@app.route("/swipe")
def swipe():
    return render_template('swipe.html')

if __name__ == "__main__":
    app.run()