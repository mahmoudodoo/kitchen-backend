from app import db
from app import app
from app.models.kitchen_model import Kitchen
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,IntegerField,SelectField
from wtforms.validators import ValidationError, DataRequired ,Regexp ,URL
from wtforms_sqlalchemy.fields  import QuerySelectField
from flask_wtf.file import FileField, FileRequired ,FileAllowed
import requests
from flask import flash

def choices_query():
    return Kitchen.query



class AddCookForm(FlaskForm):
    cook_name = StringField('Cook Name:', validators=[DataRequired()])
    kitchen = QuerySelectField(query_factory=choices_query, allow_blank=True,get_label='kitchen_name')
    video_id = StringField('Video ID:', validators=[DataRequired()])
    steps = TextAreaField('Steps:', validators=[DataRequired()])
    image = FileField('Select Image...',validators=[FileRequired(),FileAllowed(['png'], 'png Images only!')])
    submit = SubmitField('ADD')


 

class DeleteCookForm(FlaskForm):
    cook_id = StringField('Cook ID', validators=[DataRequired()])
    submit = SubmitField('DELETE')