from flask import Flask
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import mysql.connector
import shortuuid


# auth = Blueprint('auth', __name__)
# auth = Flask(__name__)

# @auth.route("/")
# @auth.route('/landing')
# def landing():
#     return render_template('L_page.html')

try:
    data = mysql.connector.connect(
    host="localhost",
    database='marketPlace',
    user="root",
    password="loba"
    )
    print(data)

    username = input("Enter Username: ")
    passwd = input("Enter Password: ")
    Email = input("Enter Email: ")
    uid = shortuuid.ShortUUID().random(length=15)
    print(uid)

    mycursor = data.cursor()

    sql = "INSERT INTO login_table (username, passwd, email, user_id) VALUES (%s, %s, %s, %s)"
    val = (username, passwd, Email, uid)
    mycursor.execute(sql, val)

    data.commit()

    print(mycursor.rowcount, "record inserted.")

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

# if __name__ == "__main__":
#     auth.run(debug=True)