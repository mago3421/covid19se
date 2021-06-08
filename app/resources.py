"""
resources.py
Forms, data, models, and controls to be used in the front-end
"""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField, SelectMultipleField, SubmitField, BooleanField
from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired, Email, Optional
from wtforms.widgets import TextArea

class pledgeForm(FlaskForm):
    # Contact information
    firstName = StringField('First name', validators=[DataRequired()])
    lastName = StringField('Last name', validators=[DataRequired()])
    organization = StringField('Organization name (optional)', validators=[Optional()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = TelField('Phone number', validators=[DataRequired()])
    # Ledger of pledged goods
    goods = SelectMultipleField('Please select good(s) to pledge', choices=[('Masks','Masks'), ('Face Shields','Face Shields'), ('Goggles','Goggles'), ('Gloves','Gloves'), ('Gowns','Gowns'), ('Sanitizer','Sanitizer'), ('Portable Shelter','Portable Shelter'), ('Food','Food'), ('Water','Water'), ('Clothing','Clothing'), ('Beds/Furniture','Beds/Furniture'), ('Other','Other')], validators=[Optional()])
    otherGoods = StringField('What other goods can you donate?', validators=[Optional()], widget=TextArea())
    # Ledger of pledged labor
    labor = SelectMultipleField('Please select the type(s) of labor you are pledging', choices=[('Delivery','Delivery'), ('Cleaning','Cleaning'), ('General volunteering','General volunteering'), ('Legal/Accounting/Administration','Legal/Accounting/Administration'), ('Software/IT','Software/IT'), ('Other','Other')], validators=[Optional()])
    otherLabor = StringField('What other labor can you volunteer?', validators=[Optional()], widget=TextArea())
    # User location
    cityLocation = StringField('In which town/city are you located?', validators=[DataRequired()])
    regionLocation = StringField('In which state/region are you located?', validators=[Optional()])
    countryLocation = StringField('In which country are you located?', validators=[DataRequired()])
    # Description/ToS/Submit
    description = StringField('Please describe in detail the goods and labor you are pledging. Please include quantities and hours per week for goods and labor, respectively. This will be used to match your pledge with requests.', validators=[DataRequired()], widget=TextArea())
    pledgeToS = BooleanField('I understand the EULA and agree to the terms and services.', validators=[DataRequired()])
    pledgeSubmit = SubmitField('Pledge support')

class requestForm(FlaskForm):
    # Contact information   
    firstName = StringField('First name', validators=[DataRequired()])
    lastName = StringField('Last name', validators=[DataRequired()])
    organization = StringField('Organization name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = TelField('Phone number', validators=[DataRequired()])
    # Ledger of requested goods    
    goods = SelectMultipleField('Please select good(s) to request', choices=[('Masks','Masks'), ('Face Shields','Face Shields'), ('Goggles','Goggles'), ('Gloves','Gloves'), ('Gowns','Gowns'), ('Sanitizer','Sanitizer'), ('Portable Shelter','Portable Shelter'), ('Food','Food'), ('Water','Water'), ('Clothing','Clothing'), ('Beds/Furniture','Beds/Furniture'), ('Other','Other')], validators=[Optional()])
    otherGoods = StringField('What other goods do you need?', validators=[Optional()], widget=TextArea())
    # Ledger of requested labor
    labor = SelectMultipleField('Please select the type(s) of labor you are requesting', choices=[('Delivery','Delivery'), ('Cleaning','Cleaning'), ('General volunteering','General volunteering'), ('Legal/Accounting/Administration','Legal/Accounting/Administration'), ('Software/IT','Software/IT'), ('Other','Other')], validators=[Optional()])    
    otherLabor = StringField('What other labor do you need?', validators=[Optional()], widget=TextArea())
    # User location
    cityLocation = StringField('In which town/city are you located?', validators=[DataRequired()])
    regionLocation = StringField('In which state/region are you located?', validators=[Optional()])
    countryLocation = StringField('In which country are you located?', validators=[DataRequired()])
    # Description/ToS/Submit
    description = StringField('Please describe in detail the goods and labor you are requesting. Please include quantities and hours per week for goods and labor, respectively. This will be used to match your request with pledges.', validators=[DataRequired()], widget=TextArea())
    requestToS = BooleanField('I understand the EULA and agree to the terms and services.', validators=[DataRequired()])
    requestSubmit = SubmitField('Request support')  
