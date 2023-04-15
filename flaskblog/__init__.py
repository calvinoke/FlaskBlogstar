from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)


#from dotenv import load_dotenv, find_dotenv
#load_dotenv(find_dotenv)




#secret key for our application..
#app.config['SECRET_KEY'] = '1b0ad53280ce712b58df13f2ca4a23e5'

# set the database uniform resource identifier for the database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#creating a database instance with the speccified database name.
db = SQLAlchemy()

bcrypt= Bcrypt()
#creating an instance of login manager
login_manager= LoginManager()
#login used is the function name of our router
login_manager.login_view= 'users.Login'
login_manager.login_message_category= 'info'
jwt = JWTManager()

mail= Mail()


def create_app(config_class = Config):

    app.config.from_object(config_class)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    with app.app_context():
        db.create_all()




    return app









