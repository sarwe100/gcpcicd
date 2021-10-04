from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Toptal  DevOps for Pythonxx file"
