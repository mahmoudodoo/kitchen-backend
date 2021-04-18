from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.admin_model import Admin


# Create regestration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6,message='Password should be at least %(min)d characters long' )])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password',message='Passwords must match')])
    submit = SubmitField('Create')

    def validate_username(self, username):
        user = Admin.query.filter_by(name=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
