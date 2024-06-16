import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://flaskmarket_user:LK90qqnZeS9kstXGijtlJgDRo9JYwlvn@dpg-cpn960g8fa8c73asv6ug-a.oregon-postgres.render.com/flaskmarket"
#
app.config['SECRET_KEY']='ec897fgh78457845754d65d'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category="info"
from Market import routes

