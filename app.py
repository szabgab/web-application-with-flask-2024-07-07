from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def main():
    return 'Hello <b>World!</b> <a href="/time">time</a> <a href="/echo">echo</a>'


@app.route("/time")
def show_time():
    return str(time.time())


# http://127.0.0.1:5000/echo?text=hello
# http://127.0.0.1:5000/echo?text=hello+world%21

@app.route("/echo")
def echo():
    app.logger.info(request.args)
    return """
<form>
<input name="text">
<input type="submit" value="Echo">
</form>
"""
