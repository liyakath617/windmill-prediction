from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route('/home')
def home():
    return render_template("home.html")
@auth.route('/predict')
def result():
    return render_template("result.html")