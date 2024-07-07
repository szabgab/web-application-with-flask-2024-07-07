from flask import Flask, request, render_template
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

# @app.route("/echo")
# def echo():
#     app.logger.info(request.args)
#     text = request.args.get("text")

#     #html = "\n" * 100
#     html = ""
#     if text:
#         html += f"You said <b>{text}</b><hr>"
    
#     html = html + """
# <form>
# <input name="text">
# <input type="submit" value="Echo">
# </form>
# """

#     return html


@app.route("/echo")
def echo():
    app.logger.info(request.args)
    text_from_user = request.args.get("text")
    
    # here comes the business logic

    return render_template("echo.html",
                           text = text_from_user
                    )