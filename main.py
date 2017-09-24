from flask import Flask, request, redirect, render_template
import html
import os

app=Flask(__name__)
app.config['DEBUG']=True

username_err=""
password_err=""
vpassword_err=""
email_err=""

@app.route("/", methods=["POST"])
def index():

    #fetch userdata from form
    username=request.form["username"]
    password=request.form["password"]
    vpassword=request.form["vpassword"]
    email=request.form["email"]

    #check username
    if not username or " " in username or len(username)<3 or len(username)>20:
        username_err="Please enter a valid username."
        return render_template("index.html",username_err=username_err)

    #check password
    elif not password or " " in password or len(password)<3 or len(password)>20:
        username_err="Please enter a valid username."
        return render_template("index.html",password_err=password_err)
    
    #check vpassword
    elif vpassword!=password:
        vpassword_err="Your passwords don't match."
        return render_template("index.html",vpassword_err=vpassword_err)

    #check email
    elif email.count("@")!=1 or email.count(".")!=1:
        email_err="Please enter a valid email address or leave blank."
        return render_template("index.html",email_err=email_err)

    else:
        return redirect("/welcome.html",username=username)
    

app.run()