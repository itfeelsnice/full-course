
from flask import Flask, redirect, render_template, request, jsonify, make_response
import psycopg2
import os
from dotenv import load_dotenv
import datetime
import smtplib
import json

load_dotenv("secret1.env")

start1 = Flask(__name__)

connect1 = psycopg2.connect(host = os.getenv("host1"),
                            database = os.getenv("database1"),
                            user = os.getenv("user1"),
                            password = os.getenv("password1"),
                            port = os.getenv("port1")
                            )

execute1 = connect1.cursor()

execute1.execute("""CREATE TABLE IF NOT EXISTS path1(
                id1 SERIAL PRIMARY KEY, 
                email1 TEXT,
                datetime1 TEXT
                )""")
connect1.commit()

@start1.errorhandler(404)
def handle_errors1(ok1):
    return render_template("error1.html")

@start1.after_request
def function_set1(response1):
    csp_rules1 = ("default-src 'self'; "
              "script-src 'self'; "
              "object-src 'none'; ")

    response1.headers["Content-Security-Policy"] = csp_rules1
    response1.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response1.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    response1.headers["Cross-Origin-Resource-Policy"] = "same-origin"

    return response1

@start1.route("/get_btn1", methods = ["GET", "POST"])
def get_btn1():
    get1 = request.json
    get2 = get1.get("button_id1")

    if get2 == "btn22":
        send_response = make_response()

        list1 = [0]

        with open("json1.json", "r") as read1:
            list1 = json.load(read1)

        list1.append(len(list1) + 1)
        b1 = list1[-1]

        with open("json1.json", "w") as append1:
            json.dump(list1, append1)

        send_response.set_cookie(
            "cookie1",
            f"cookie{b1}",
            max_age = 3600,
            path = "/",
            secure = False,
            httponly = True,
            samesite = "strict",
        )

        return send_response
    
@start1.route("/", methods = ["GET", "POST"])
def function1():
    if request.method == "POST":
        email1 = request.form.get("input1")
        datetime1 = datetime.datetime.now()
        execute1.execute("INSERT INTO path1 (email1, datetime1) VALUES (%s, %s)", (email1, datetime1))
        connect1.commit()
        return render_template("html1.html")
    
    return render_template("html1.html")

@start1.route("/check_cookie1", methods = ["GET", "POST"])
def get1():
    cookie_exist1 = request.cookies.get("cookie1")
    if cookie_exist1:
        return "set_cookie1"
    
@start1.route("/htmlex")
def html1():
    return render_template("html2.html")

@start1.route("/cssex")
def css1():
    return render_template("css2.html")

@start1.route("/jsex")
def js1():
    return render_template("javascript2.html")

@start1.route("/gitex")
def git1():
    return render_template("git1.html")

@start1.route("/sqlex")
def sql1():
    return render_template("sql1.html")

@start1.route("/cmdex")
def cmd1():
    return render_template("cmd1.html")

@start1.route("/ntex")
def nt1():
    return render_template("network1.html")

@start1.route("/pyex")
def py1():
    return render_template("python2.html")

start1.run(debug=True)
connect1.cancel()

# many of the things writed in this commit i didnt knew before so i dont know how to fully use them yet
# but i got an idea about them like fetch in javascript (headers, body and method and that i am giving the
# information to the route name "/etc")

# or the json things i knew about them but i havnt used them in a long time so i forgot most of the things about them

# after this project is done i will practice with them because this is just so new to me like its insane
