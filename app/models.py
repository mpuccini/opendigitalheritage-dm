# model.py
from wtforms import SubmitField, BooleanField, StringField, PasswordField, TextAreaField, FileField, SelectField, DateField, validators
from flask_wtf import FlaskForm
#from wtforms.fields import SubmitField, BooleanField, StringField, PasswordField, TextAreaField, FileField, SelectField, DateField
from flask_wtf.file import FileField, FileAllowed, FileRequired


class InsertPubForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  year = DateField('Year', format='%Y')
  license_url = StringField('License URL')
  pub = FileField('Publication')
  submit = SubmitField('Submit')

class InsertModelForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  objtype = '3Dmodel'
  year = DateField('Year', format='%Y')
  license_url = StringField('License URL')
  coordinates = StringField('Coordinates')
  model = FileField('Model', validators=[
    FileRequired(),
    FileAllowed(['ply', 'nxz'], 'Sorry, ply and nxz only allowed!')
    ])
  submit = SubmitField('Submit')


'''
class uploadObjForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  objtype = '3Dmodel'
  year = DateField('Year', format='%Y')
  license_url = StringField('License URL')
  coordinates = StringField('Coordinates')
  obj = FileField('Object')
  store_type = SelectField(u'Store type', choices=[('fs', 'HeritageScience File System'), 
                                                      ('s3', 'Amazon S3 Object Storage')])
  submit = SubmitField('Submit')
'''



class InsertImgForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  author = StringField('Author', [validators.DataRequired()])
  project = StringField('Project', [validators.DataRequired()])
  year = DateField('Year', format='%Y')
  license_url = StringField('License URL')
  coordinates = StringField('Coordinates')
  img = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Sorry, images only (jp[e]g and png)!')
    ])
  submit = SubmitField('Submit')  

class searchForm(FlaskForm):
  query = StringField('', [validators.DataRequired()])
  submit = SubmitField('Submit')  

class testForm(FlaskForm):
  photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
  submit = SubmitField('Submit')


