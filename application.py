import os
from cs50 import SQL
import datetime
from flask import Flask, flash, redirect,render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology



# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses are not cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem instead of signed cookie
app.config["SESSION_FILE_DIR"]= mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///addressbook.db")


@app.route("/login",methods=["GET", "POST"])
def login():
    '''Log user in'''

    # Forget any user_id

    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")


        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

       # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/")
@login_required
def index():
    contacts = db.execute("SELECT * FROM contacts WHERE user_id = ?", session["user_id"])
    return render_template("index.html", contacts = contacts)





@app.route("/new", methods=["GET","POST"])
@login_required
def new():

    if request.method == "POST":
        # Create a table storing the details of the new contact

        # db.execute("CREATE TABLE contacts (user_id INTEGER NOT NULL, name TEXT NOT NULL, address TEXT NOT NULL, email TEXT NOT NULL, number TEXT NOT NULL)")

        # insert the data filled in into the table

        name= request.form.get("name")
        address= request.form.get("address")
        email= request.form.get("email")
        number = request.form.get("number")


        db.execute("INSERT INTO contacts (user_id, name, address, email, number) VALUES (?,?,?,?,?)", session["user_id"], name, address, email, number)

        return redirect ("/")

    # User reach route via GET (as by clicking a link or via redirect)
    elif request.method == "GET":
        return render_template("new.html")



@app.route("/search", methods=["GET","POST"])
@login_required
def search():
    if request.method == "POST":
        search_result = request.form.get("search")

       # Query databse for anything like the search_result

        search_rows = db.execute("SELECT * from contacts WHERE user_id = ? and name LIKE ?", session["user_id"], search_result)

        return render_template("index.html", contacts = search_rows)




@app.route("/register", methods=["GET","POST"])
def register():
    # If user submit the register form

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        email = request.form.get("email")


        if password != confirmation:
            return apology("Password do not match", 403)


        # Query database for username

        user_name_rows = db.execute("SELECT * from users where username=?", username)

        # check if username already exists in database
        if len(user_name_rows) == 1:
            return apology("Username is taken. Please use a different username", 400)


        # Insert new user and hashed password into the database

        hashed_password = generate_password_hash(password)

        db.execute("INSERT INTO users (username, hash, email) VALUES (?, ?,?)", username, hashed_password, email)

        # redirect user to log in
        return redirect("/login")


    # User reached route via GET (ie clicking a link or via redirect)
    else:
        return render_template("register.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")


@app.route("/contact")
def contact():
   return render_template("contact.html")