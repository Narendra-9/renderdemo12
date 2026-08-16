import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://marketdb_fltp_user:jeQA0VbCsSeLnFS5Iz7p34aOdFuvEEQX@dpg-da0s2t5bedkc73bg34n0-a/marketdb_fltp"
#
app.config['SECRET_KEY']='ec897fgh78457845754d65d'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category="info"
from Market import routes

