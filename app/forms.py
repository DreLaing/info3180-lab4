from flask_wtf import FlaskForm
from wtforms import FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
class UploadForm(FlaskForm):
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])


