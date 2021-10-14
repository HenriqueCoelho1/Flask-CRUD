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


class User(db.Model):
    __tablename__ = "usr"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)

    def __init__(self, username, name, email, cpf):
        self.username = username
        self.name = name
        self.email = email
        self.cpf = cpf


@app.route('/')
def index():
    all_data = User.query.all()
    return render_template("index.html", users=all_data)


@app.route('/submit', methods=["POST"])
def submit_form():
    if request.method == "POST":
        username = request.form["username"]
        name = request.form["name"]
        email = request.form["email"]
        cpf = request.form["cpf"]
        # print(username, name, email, cpf)
        if username == "" or name == "" or email == "" or cpf == "":
            return render_template("index.html", message="Please enter required fields")
        if db.session.query(User).filter(User.username == username).count() == 0:
            data = User(username, name, email, cpf)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        else:
            return render_template("index.html", message=f"This {name} is already exist")


@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        my_data = User.query.get(request.form.get("id"))
        # my_data.username = request.form["username"]
        # my_data.name = request.form["name"]
        # my_data.email = request.form["email"]

        db.session.commit()
        return render_template("success.html")


@app.route("/delete/<id>/", methods=["GET", "POST"])
def delete(id):
    my_data = User.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return render_template("success.html")


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
