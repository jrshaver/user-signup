from flask import Flask, request, redirect, render_template
import html 
import os

app=Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def welcome():
    
    username_err=""
    password_err=""
    vpassword_err=""
    email_err=""

    #fetch userdata from form
    username=html.escape(request.form["username"])
    password=html.escape(request.form["password"])
    vpassword=html.escape(request.form["vpassword"])
    email=html.escape(request.form["email"])

    #check username
    if not username or " " in username or len(username)<3 or len(username)>20:
        username_err="Please enter a valid username."

    #check password
    if not password or " " in password or len(password)<3 or len(password)>20:
        password_err="Please enter a valid password."
    
    #check vpassword
    if vpassword!=password:
        vpassword_err="Your passwords don't match."

    #check email
    if email:
        if email.count("@")!=1 or email.count(".")!=1:
            email_err="Please enter a valid email address or leave blank."

    if not username_err and not password_err and not vpassword_err:
        return render_template("/welcome.html",username=username)
    else:
        return render_template("index.html", username=username,email=email,username_err=username_err,password_err=password_err,vpassword_err=vpassword_err,email_err=email_err)
    

app.run()