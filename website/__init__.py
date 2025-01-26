from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user


DB_NAME = "database.db"

db = SQLAlchemy() # create instance

def create_app():
    app = Flask(__name__) # initialize flask
    app.config["SECRET_KEY"] = "sdife3fwifnweui"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    # initialize app
    db.init_app(app)

    # import and register blueprints

    from  .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # initialize login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # import User here to avoid circular import
    from .models import User


    # user loader for login manager
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.context_processor
    def inject_user(): # makes current_user accessible as user in templates
        from flask_login import current_user
        return {"user": current_user}
    
    return app


def create_database(app):
    '''create database within app context'''
    with app.app_context():
        db.create_all()





