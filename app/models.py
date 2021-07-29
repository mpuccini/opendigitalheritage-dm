# model.py
from wtforms import SubmitField, BooleanField, StringField, PasswordField, TextAreaField, validators
from flask_wtf import FlaskForm
from wtforms.fields import FileField, SelectField, DateField

class InsertPubForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  year = DateField('Year', format='%Y')

  pub = FileField('Publication')
  submit = SubmitField('Submit')

class InsertModelForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  objtype = '3Dmodel'
  year = DateField('Year', format='%Y')

  coordinates = StringField('Coordinates')
  model = FileField('Model')
  submit = SubmitField('Submit')

class InsertImgForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  year = DateField('Year', format='%Y')

  coordinates = StringField('Coordinates')
  img = FileField('Image')
  submit = SubmitField('Submit')  

class SearchPubForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  submit = SubmitField('Submit')  

class SearchImgForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  submit = SubmitField('Submit')  

class SearchModelForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  submit = SubmitField('Submit')  

class SearchInventoryForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  submit = SubmitField('Submit')  




