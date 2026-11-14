
from flask import Flask, redirect, render_template, request
import psycopg2
import os
from dotenv import load_dotenv
import datetime
import smtplib

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

@start1.route("/", methods = ["GET", "POST"])
def function1():
    if request.method == "POST":
        email1 = request.form.get("input1")
        datetime1 = datetime.datetime.now()
        execute1.execute("INSERT INTO path1 (email1, datetime1) VALUES (%s, %s)", (email1, datetime1))
        connect1.commit()
        return render_template("html1.html")
    
    return render_template("html1.html")

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

