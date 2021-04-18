
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import  DataRequired
from flask_wtf.file import FileField, FileRequired ,FileAllowed



# Create Login Form Using wtforms module
class AddKitchenForm(FlaskForm):
    kitchen_name = StringField('Kitchen Name:', validators=[DataRequired()])
    image = FileField('Select Image...',validators=[FileRequired(),FileAllowed(['png'], 'png Images only!')])
    submit = SubmitField('ADD')


class DeleteKitchenForm(FlaskForm):
    kitchen_id = StringField('Kitchen ID', validators=[DataRequired()])
    submit = SubmitField('DELETE')