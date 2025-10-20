from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/predict')
def home():
    return render_template("home.html")
@views.route('/result')
def result():
    return render_template("result.html")