from flask import request, render_template, session, redirect, url_for, current_app, send_file
from . import main
from .. import db
from .forms import FoxOrderForm
from ..models import ProductCategory, Product
# from ..models import User
# from ..email import send_email

"""
TODO:
* Add home page for Fox Furniture
* Add category page for Fox Furniture
* Add confirmation page for Fox Furniture


HISTORY:

"""

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

@main.route("/projects/fox_furniture_order/", methods=["GET", "POST"])
def fox_order_form():
    form = FoxOrderForm()
    form.product_category.choices = [(row.id, row.name) for row in \
                            ProductCategory.query.all()]

    if request.method == "GET":
        return render_template("fox_order.html", form=form)
    
    else:
        #form.validate_on_submit():
        # TODO - store order in db
        return redirect(url_for("main.fox_order_confirmation"))

@main.route("/projects/fox_furniture_order/order_confirmation/", methods=["GET"])
def fox_order_confirmation():
    return render_template("fox_order_confirm.html")

@main.route("/projects/fox_furniture/catalog/")
def fox_catalog():
    return render_template("fox_catalog.html")

@main.route("/projects/fox_furniture/api/types")
def db_get_product_categories():
    
    product_category_list = ProductCategory.query.all()

    return render_template("product_categories.html", product_category_list=product_category_list)

@main.route("/projects/fox_furniture/api/products")
def db_get_products():

    products = Product.query.all()

    return render_template("products.html", products=products)