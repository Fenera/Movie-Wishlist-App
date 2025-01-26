from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, current_user, login_required

auth = Blueprint('auth', __name__)


# login page
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # check if information is valid

        user = User.query.filter_by(username=username).first()
        
        # check if user with that username exists
        if user:
            # password check
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password is incorrect, try again!", category="error")
        else:
            flash("Username does not exist, try again", category="error")


    return render_template("login.html", user=current_user)

# sign up page
@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():

    if request.method == 'POST': # register

        # get information from entry
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password') # first password entered
        password2 = request.form.get('password2') # confirmation password
        
        user_by_email = User.query.filter_by(email=email).first() # fetches the first user object that matches the provided email
        user_by_username = User.query.filter_by(username=username).first() # same as above but for username
    
        # remember information so input boxes don't clear when refreshing or flashing errors
        if not email or not username or not password1 or not password2: # check for empty fields
            flash("Please fill out all boxes", category="danger")
            # store the current values in the session
            session['email'] = email
            session['username'] = username
            session['password1'] = password1
            session['password2'] = password2
            # redirect to the same page(might be unnecessary)
            return redirect(url_for('auth.sign_up'))      

        if user_by_email: # a user exists in the db with the same email
            flash("Email is already in use", category="danger")
        elif user_by_username:
            flash("Username already in use", category="danger")
        elif len(username) < 4: # length at least 4
            flash("Username must be at least 4 characters")
        elif len(email) < 4: # length at least 4
            flash("Email must be at least 4 characters", category="danger")
        elif password1 != password2: # original password and confirmation password don't match
            flash("Password don't match", category="danger")
        elif len(password1) < 7: # length at least 7
            flash("Password must be at least 7 characters") 
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method="pbkdf2:sha256")) # hash the password(one-way function so password -> hash but not hash -> password) for security purposes(more info: https://www.youtube.com/watch?v=deNIgVyDyJY)   
            
            # add user with credentials to db
            db.session.add(new_user)
            db.session.commit() 
            login_user(new_user, remember=True)
            flash("Account Created!", category="success")
            # delete session data after account creation
            session.pop("username", None)
            session.pop("email", None)
            session.pop("password1", None)
            session.pop("password2", None)

            # redirect to home page after signing in
            return redirect(url_for('views.home'))
        
    # if GET request(page load or refresh) check if there's data already in the session
    # default to empty('') if nothing in session
    username = session.get('username', '')
    email = session.get('email', '')
    password1 = session.get('password1', '')
    password2 = session.get('password2', '')

    return render_template('sign_up.html', user=current_user, username=username, email=email, password1=password1, password2=password2)


# log out 
# must be logged in(@ logged_in)
# redirect to login page

