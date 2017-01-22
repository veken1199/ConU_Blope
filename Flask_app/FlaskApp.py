from flask import Flask,render_template
#import pypyodbc
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('login.html')


@app.route("/swipe")
def swipe():
    return render_template('swipe.html')

if __name__ == "__main__":
    app.run()