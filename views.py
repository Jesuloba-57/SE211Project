from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route("/")
def L_page():
    return render_template('index.html')


@views.route("/about")
def about():
    return render_template('about.html')


@views.route("/cart")
def cart():
    return render_template('cart.html')

@views.route("/seller")
def seller():
    return render_template('seller.html')