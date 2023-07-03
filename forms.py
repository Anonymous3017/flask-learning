from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, RadioField, SelectField
from email_validator import validate_email, EmailNotValidError

from wtforms import validators, ValidationError, SubmitField

class ContactForm(Form) :
    name = StringField("Name of Student", [validators.DataRequired("Please enter your name.")])
    Gender = RadioField('Gender', choices= [('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")

    email = StringField("Email", [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])

    Age = IntegerField("age")
    language = SelectField('Languages', choices = [('cpp', 'C++'), ('py', 'Python'), ('js', 'JavaScript')])
    submit = SubmitField("Send")