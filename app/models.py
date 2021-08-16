# model.py
from wtforms import SubmitField, BooleanField, StringField, PasswordField, TextAreaField, FileField, DateField, validators
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired



class InsertPubForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  authorship = StringField('Authorship', [validators.DataRequired()])
  license = StringField('License')


  project_name = StringField('Name', [validators.DataRequired()])
  project_year = DateField('Year', format='%Y')
  project_url = StringField('URL')
  project_partners = StringField('Partners')

  obj = FileField('Publication', validators=[
    FileRequired(),
    FileAllowed(['pdf', 'doc', 'docx', 'odt'], 'Sorry, pdf, doc, docx  and odt only allowed!')
  ])

  submit = SubmitField('Submit')


class InsertModelForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  authorship = StringField('Authorship', [validators.DataRequired()])
  coordinates = StringField('Coordinates')
  license = StringField('License')


  project_name = StringField('Name', [validators.DataRequired()])
  project_year = DateField('Year', format='%Y')
  project_url = StringField('URL')
  project_partners = StringField('Partners')

  obj = FileField('Model', validators=[
    FileRequired(),
    FileAllowed(['ply', 'nxz'], 'Sorry, ply and nxz only allowed!')
  ])

  submit = SubmitField('Submit')



class InsertImgForm(FlaskForm):
  title = StringField('Title', [validators.DataRequired()])
  description = TextAreaField('Description')
  authorship = StringField('Authorship', [validators.DataRequired()])
  coordinates = StringField('Coordinates')
  license = StringField('License')


  project_name = StringField('Name', [validators.DataRequired()])
  project_year = DateField('Year', format='%Y')
  project_url = StringField('URL')
  project_partners = StringField('Partners')

  obj = FileField('Image', validators=[
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


