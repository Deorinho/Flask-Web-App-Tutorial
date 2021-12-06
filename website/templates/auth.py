from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)
'''This is the basic structure of creating a webpage. first we call the route using @
then we create the instance which will be the suffix of the address
within the function we add text'''


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")


