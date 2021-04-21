from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


db=SQLAlchemy()
app = Flask(__name__)
api=Api(app)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:malosutra123@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate=Migrate(app,db)

from app import routes
