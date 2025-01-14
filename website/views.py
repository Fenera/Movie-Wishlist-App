from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


#home page
@views.route('/', methods= ['POST', 'GET'])
# home page not accessible if logged out
def home():

    return render_template('home.html', user=current_user)

# wishlist
@views.route('/wishlist', methods = ['POST', 'GET'])
def wishlist():
    return render_template('wishlist.html')