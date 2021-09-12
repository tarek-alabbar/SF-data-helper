from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<h1>Test login</h1>"


@auth.route('/logout')
def logout():
    return "<h1>Test logout</h1>"
