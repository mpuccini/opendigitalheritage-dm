# app.py
#!bin/python
from flask import Flask, request, render_template
from werkzeug.datastructures import FileStorage
from models import InsertPdfForm
from flask_bootstrap import Bootstrap
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("mongodb+srv://giacomo:12345@cluster0.8buoe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['pocenea'] 

PDFs = db['PDFs']


app.config.from_mapping(
    SECRET_KEY=b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insertOption')
def insertOption():
    return render_template('insertOption.html')

@app.route('/insertPDF', methods=['GET', 'POST'])
def insertPDF():
    form = InsertPdfForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        name = request.form['nome']
        pdf=request.files['pdf']
        filepath="C:/filepdfjpeg/"
        PDFs.insert_one({'nomeOpera': name, 'nomePDF':pdf.filename , 'PathPDF': filepath+pdf.filename })
        return render_template('uploadDone.html')
    return render_template('uploadPDF.html',form=form)






if __name__ == '__main__':
    app.run()
