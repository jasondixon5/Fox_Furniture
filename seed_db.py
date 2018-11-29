import csv
import os
import sqlalchemy as sa

from app.models import ProductCategory
from manage import db

# Store data from source file
filename = "store_db_initial_sources.csv"
product_category_list = []

with open(filename) as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        category = row["Category"]
        product_category_list.append(category)

product_category_list = list(set(product_category_list))

# Create row objects and add to db
category_objects = []
for cat_name in product_category_list:
    obj = ProductCategory(name=cat_name, level=1)
    category_objects.append(obj)

db.session.add_all(category_objects)
db.session.commit()