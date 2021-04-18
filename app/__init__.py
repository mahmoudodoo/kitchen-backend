from app.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'


db.create_all()
from app.views import home,kitchen_view,register_view,login_view,cook_view
from app.models import admin_model,cook_model,kitchen_model
from app.api import admin_api,user_api,cook_api,kitchen_api