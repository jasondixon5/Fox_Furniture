#!/usr/bin/env python
import os
from app import create_app, db
#from app.models import User, Role
from app.models import ProductCategory
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    #return dict(app=app, db=db, User=User, Role=Role)
    #return dict(app=app, db=db)
    return dict(app=app, db=db, ProductCategory=ProductCategory)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def seed():
    """See database with initial data"""
    import csv
    from app.models import ProductCategory

    # Store data from source file
    filename = "db_seed/store_db_initial_sources.csv"
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

@manager.command
def seed_products():
    """See products table with initial data"""
    import csv
    from app.models import Product

    # Store data from source file
    filename = "db_seed/store_db_initial_sources.csv"
    product_category_dict = {"Office Supplies": 1,
                            "Technology": 2,
                            "Furniture": 3}
    product_name_list = []
    product_category_tuples= []

    with open(filename) as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            category = row["Category"]
            product_name = row["Product Name"]
            category_id = product_category_dict.get(category, 0)
            if product_name not in product_name_list:
                # add to name list to prevent dupicate adds to product table
                product_name_list.append(product_name)
                product_category_tuples.append((product_name, category_id))
            else:
                continue

    # Create row objects and add to db
    product_objects = []
    for name_id_tup in product_category_tuples:
        obj = Product(name=name_id_tup[0], category_id=name_id_tup[1])
        product_objects.append(obj)

    db.session.add_all(product_objects)
    db.session.commit()

if __name__ == '__main__':
    manager.run()