from flask import Flask, render_template, session, redirect, url_for, flash, Response, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)
ENV = "dev"
if ENV == "dev":
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost:5432/teste"
else:
    app.debug = False
    app.config["SQLALCHEMY_DATABASE_URI"] = ""

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class FeedBack(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit', methods=["POST"])
def submit_form():
    if request.method == "POST":
        customer = request.form["customer"]
        dealer = request.form["dealer"]
        rating = request.form["rating"]
        comments = request.form["comments"]
        # print(customer, dealer, rating, comments)
        if customer == "" or dealer == "":
            return render_template("index.html", message="Please enter required fields")
        if db.session.query(FeedBack).filter(FeedBack.customer == customer).count() == 0:
            data = FeedBack(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        else:
            return render_template("index.html", message="This name is already exist")


@app.route('/user/<name>')
def user_id(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run()
