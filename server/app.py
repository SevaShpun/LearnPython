from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.sql_login
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
app.secret_key = config.secret_key
db = SQLAlchemy(app)


if __name__ == '__main__':
    from views import *
    app.run(host="0.0.0.0")
