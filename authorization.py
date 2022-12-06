from flask import Blueprint, render_template, request, flash, redirect, url_for
from db_model import User
from __init__ import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import shortuuid

auth = Blueprint('auth', __name__)

@auth.route("/")
@auth.route('/home')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.landing'))
    else:
        return render_template('index.html')
    
@auth.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
         email = request.form.get('email')
         password = request.form.get('password1')

         user = User.query.filter_by(email=email).first()
         if not user:
             flash('Email does no found.', category='error')
             return render_template('login.html')
             # user=current_user
         if not check_password_hash(user.password, password):
             flash('Incorrect password, try again.', category='error')
             return render_template('login.html') 
        
         flash('Logged in successfully!', category='success')
         login_user(user, remember=True)
         return render_template('index.html')
    
     return render_template('login.html')
         # else:
         #     flash('Incorrect password, try again.', category='error')
         # # else:
         #     flash('Email does not exist.', category='error')

     # return render_template('login.html', user=current_user)


# @auth.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('auth.landing'))


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email Already Exists.', category='error')
            return render_template('signup.html')

        fname = request.form.get('fname')
        lname = request.form.get('lname')
        password1 = str(request.form.get('password1'))
        password2 = str(request.form.get('password2'))
        uid = shortuuid.ShortUUID().random(length=15)

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            new_user = User(id=uid, email=email, password=generate_password_hash(password1, method='pbkdf2:sha1', salt_length=8))
            db.session.add(new_user)
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            db.session.commit()
            message="Welcome "+fname
            return render_template ('index.html', message=message)

    return render_template('signup.html', user=current_user)