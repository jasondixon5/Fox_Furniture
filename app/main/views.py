from flask import render_template, session, redirect, url_for, current_app, send_file
from . import main
from .. import db
# from ..models import User
# from ..email import send_email
# from .forms import NameForm

@main.route('/', methods=['GET'])
def index():
    
    return render_template("index.html")

@main.route(
    "/static/docs/Jason_Dixon_Resume.pdf", 
    methods=["GET"])
def send_resume():
    
    return send_file(
        "./static/docs/Jason_Dixon_Resume.pdf",
        attachment_filename = "Jason_Dixon_Resume.pdf")

@main.route("/projects", methods=["GET"])
def projects():

    return render_template("projects.html")


