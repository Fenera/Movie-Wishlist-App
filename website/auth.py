from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, current_user

auth = Blueprint('auth', __name__)


# login page
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

# sign up page
@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():

    if request.method == 'POST': # register
        flash("Test Flash Message", category="success")  # Test Flash Message
        # get information from entry
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password') # first password entered
        password2 = request.form.get('password2') # confirmation password
        
        user_by_email = User.query.filter_by(email=email).first() # fetches the first user object that matches the provided email
        user_by_username = User.query.filter_by(username=username).first() # same as above but for username

        if user_by_email: # a user exists in the db with the same email
            flash("Email is already in use", category="error")
        elif user_by_username:
            flash("Username already in use", category="error")
        elif len(username) < 4: # length at least 4
            flash("Username must be at least 4 characters")
        elif len(email) < 4: # length at least 4
            flash("Email must be at least 4 characters", category="error")
        elif password1 != password2: # original password and confirmation password don't match
            flash("Password don't match", category="error")
        elif len(password1) < 7: # length at least 7
            flash("Password must be at least 7 characters") 
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method="pbkdf2:sha256")) # hash the password(one-way function so password -> hash but not hash -> password) for security purposes(more info: https://www.youtube.com/watch?v=deNIgVyDyJY)   
            
            # add user with credentials to db
            db.session.add(new_user)
            db.session.commit() 
            login_user(new_user, remember=True)
            flash("Account Created!", category="success")

            # redirect to home page after signing in
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)


# log out 
# must be logged in(@ logged_in)
# redirect to login page


