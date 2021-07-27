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
  extension = SelectField(u'File extension', choices=[('pdf', '.pdf Portable Document Format'), 
                                                      ('doc', '..doc Microsoft Word Format'),
                                                      ('docx','.docx Microsoft Word Open XML Format'),
                                                      ('odt', '.odt Open Document Text'),
                                                      ('tex','.tex LaTeX source')])
  pub = FileField('Publication')
  store_type = SelectField(u'Store type', choices=[('fs', 'HeritageScience File System'), 
                                                      ('s3', 'Amazon S3 Object Storage')])
  submit = SubmitField('Submit')

class InsertModelForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  objtype = '3Dmodel'
  year = DateField('Year', format='%Y')
  extension = SelectField(u'File extension', choices=[('ply', '.ply Poligon File Format'), 
                                                      ('nxz', '.nxz Nexus compressed ')])
  coordinates = StringField('Coordinates')
  model = FileField('Model')
  store_type = SelectField(u'Store type', choices=[('fs', 'HeritageScience File System'), 
                                                      ('s3', 'Amazon S3 Object Storage')])
  submit = SubmitField('Submit')

class InsertImgForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  year = DateField('Year', format='%Y')
  extension = SelectField(u'File extension', choices=[('jpeg', '.jpeg '), 
                                                      ('png', '.png ')])
  coordinates = StringField('Coordinates')
  img = FileField('Image')
  store_type = SelectField(u'Store type', choices=[('fs', 'HeritageScience File System'), 
                                                      ('s3', 'Amazon S3 Object Storage')])
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




