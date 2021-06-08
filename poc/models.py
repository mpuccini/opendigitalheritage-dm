# model.py
from wtforms import SubmitField, BooleanField, StringField, PasswordField, TextAreaField, validators
from flask_wtf import Form
from wtforms.fields.simple import FileField


class InsertPdfForm(Form):
  nome = StringField('nome', [validators.DataRequired()])
  pdf = FileField('pdf')
  submit = SubmitField('Submit')

class InsertModelForm(Form):
  nome = StringField('nome', [validators.DataRequired()])
  model = FileField('model')
  submit = SubmitField('Submit')






