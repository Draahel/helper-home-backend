from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config.db_credentials import db_config

app = Flask(__name__)

db_user = db_config['db_user']
db_pass = db_config['db_pass']
db_host = db_config['db_host']
db_name = db_config['db_name']

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# app.secret_key = "movil2"

db = SQLAlchemy(app)

ma = Marshmallow(app)