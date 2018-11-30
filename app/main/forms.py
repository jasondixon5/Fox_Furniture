from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class FoxOrderForm(FlaskForm):
    first_name = StringField(
        'First Name', 
        validators=[DataRequired()],
        id="requestor_first_name")
    last_name =  StringField(
        'Last Name', 
        validators=[DataRequired()],
        id="requestor_last_name")
    email_address = StringField(
        'Email Address', 
        validators=[DataRequired()],
        id="requestor_email")
    product_category = SelectField(
        "Category", 
        validators=[DataRequired()],
        id="select_product_category")
    
    submit = SubmitField('Submit')
