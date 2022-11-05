from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hey Mariam. You're learning and doing well</p>"