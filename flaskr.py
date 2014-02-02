# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create application
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    """
    DB Connect function

    """
    return sqlite3.connect(app.config['DATABASE'])

if "__main__" == __name__:
    app.run()
