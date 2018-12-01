
from . import db

"""Model definitions for store order form and catalogue
"""

class ProductCategory(db.Model):
    """Table to store categories of products
    e.g., furniture, office supplies
    """
    __tablename__ = "product_categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    # Level allows subdivision of categories
    level = db.Column(db.SmallInteger, nullable=False)
    products = db.relationship(
        "Product", 
        backref="category", 
        lazy=True)

    def __repr__(self):
        return "Category {} (Level {})".format(self.name, self.level)

class Product(db.Model):
    """
    Table to store products
    """
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    # Category is FK
    category_id = db.Column(
        db.Integer, 
        db.ForeignKey("category.id"),
        nullable=False)

    def __repr__(self):
        return "Product {}".format(self.name)