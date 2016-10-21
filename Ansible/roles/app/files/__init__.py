#!/usr/bin/env python

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return render_template("view.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
