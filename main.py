from flask import Flask, request, redirect, render_template
import html, os

app=Flask(__name__)
app.config['DEBUG']=True


@app.route("/")
def index():
    return render_template("index.html")