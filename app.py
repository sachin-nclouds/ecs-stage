from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! this is new deployment 2 let check it 2 let check it</p>"
