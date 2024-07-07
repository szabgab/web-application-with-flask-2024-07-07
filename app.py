from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def main():
    return 'Hello <b>World!</b> <a href="/time">time</a> <a href="/echo">echo</a>'


@app.route("/time")
def show_time():
    return str(time.time())


@app.route("/echo")
def echo():
    return """
<form>
<input name="text">
</form>
"""
