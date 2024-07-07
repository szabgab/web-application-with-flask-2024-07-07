from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello <b>World!</b>"


@app.route("/time")
def show_time():
    return time.time()
