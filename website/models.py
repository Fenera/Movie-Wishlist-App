from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# create User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, 
                   primary_key=True)
    username = db.Column(db.String(150), # max character limit
                         unique=True, 
                         nullable=False)
    email = db.Column(db.String(150), 
                      unique=True, 
                      nullable=False)
    password = db.Column(db.String(150),
                         nullable=False)
    
