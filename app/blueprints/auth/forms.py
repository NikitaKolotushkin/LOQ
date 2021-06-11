from flask_wtf import FlaskForm
from wtforms import PasswordField, IntegerField, validators, SubmitField, Form
from wtforms_components import EmailField

from app.models import User


class SignupForm(FlaskForm):
    email = EmailField()
    password = PasswordField()

    submit = SubmitField()
