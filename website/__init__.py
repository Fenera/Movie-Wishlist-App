from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # initialize flask
    app.config["SECRET_KEY"] = "sdife3fwifnweui"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"


    db.init_app(app)

    # import and register blueprints

    from  .views import views

    app.register_blueprint(views, url_prefix="/")

    return app


