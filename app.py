from flask import Flask
from Models.model import *


app=Flask(__name__)

app.config['SECRET_KEY']="BOX"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///grocery_store2.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False  #optional


db.init_app(app)

with app.app_context():
    db.create_all()



