from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = "2b48230b6dc97209471d61c9"

from market import routes