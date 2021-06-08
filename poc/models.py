# model.py
from wtforms import SubmitField, BooleanField, StringField, PasswordField, TextAreaField, validators
from flask_wtf import Form
from wtforms.fields import FileField, SelectField


class InsertPdfForm(Form):
  title = StringField('Title', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  pdf = FileField('Pdf')
  submit = SubmitField('Submit')

class InsertModelForm(Form):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  extension = SelectField(u'File extension', choices=[('ply', '.ply Poligon File Format'), ('nxz', '.nxz Nexus compressed ')])
  model = FileField('Model')
  submit = SubmitField('Submit')






