from flask import render_template, session, redirect, url_for, current_app
from . import main
from .. import db
# from ..models import User
# from ..email import send_email
# from .forms import NameForm

@main.route('/', methods=['GET'])
def index():
    
    return render_template("index.html")

def projects():

    return render_template("projects.html")
