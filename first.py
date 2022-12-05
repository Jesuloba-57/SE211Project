from flask import Flask
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from connection import login_table


auth = Blueprint('auth', __name__)
auth = Flask(__name__)
auth.config['SECRET_KEY'] = 'hkjdhkfdncjndsfhds'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')
        db = login_table()
        result = db.log_in(email, password)
        if result:
            flash('Logged in successfully!', category='success')
            login_user(user, remember=True)
            return render_template('index.html')
        else:
            flash('User Not Found.', category='error')
            return render_template('login.html')
    return render_template('login.html')


    #     user = db.query.filter_by(email=email).first()
    #     if not user:
    #         flash('Email does not exist.', category='error')
    #         return render_template('login.html') 
    #         # user=current_user
    #     if not check_password_hash(user.password, password):
    #         flash('Incorrect password, try again.', category='error')
    #         return render_template('login.html') 
        
    #     flash('Logged in successfully!', category='success')
    #     login_user(user, remember=True)
    #     return render_template('home.html')
    
    return render_template('login.html')
        # else:
        #     flash('Incorrect password, try again.', category='error')
        # # else:
        #     flash('Email does not exist.', category='error')

    # return render_template('login.html', user=current_user)


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
     if request.method == 'POST':
        email = request.form.get('email')
        user_name = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(user_name) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            sign_up(user_name, password2, email, 1)
            flash('Account created!', category='success')
            return (redirect(url_for('auth.login')))

     return render_template('signup.html')

@auth.route("/")
@auth.route('/landing')
def landing():
    return render_template('login.html')

@auth.route('/product')
def product():
    return render_template('products.html')


if __name__ == "__main__":
    auth.run(debug=True)