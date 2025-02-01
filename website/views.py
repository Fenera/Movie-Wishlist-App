from flask import Blueprint, render_template
from flask_login import login_required, current_user
from dotenv import load_dotenv
import os



views = Blueprint('views', __name__)

load_dotenv() # load environment variables from .env

api_key = os.getenv("API_KEY") 
# note to self: pass api key for each dependent page


#home page
@views.route('/', methods= ['POST', 'GET'])
@login_required
# home page not accessible if logged out
def home():
    return render_template('home.html', user=current_user, api_key=api_key) # pass api_key so it is available in .js

# wishlist page
@views.route('/wishlist', methods = ['POST', 'GET'])
@login_required
def wishlist():
    return render_template('wishlist.html', api_key=api_key)