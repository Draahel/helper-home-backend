from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

db_user = 'your_user'
db_pass = 'your_pass'
db_host = 'your_host'
db_name = 'your_dbname'

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# app.secret_key = "movil2"

db = SQLAlchemy(app)

ma = Marshmallow(app)