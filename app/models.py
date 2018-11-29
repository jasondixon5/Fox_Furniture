
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

    def __repr__(self):
        return "Category {} (Level {})".format(self.name, self.level)

