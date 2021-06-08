# app.py
#!bin/python
from flask import Flask, request, render_template
from models import InsertPdfForm, InsertModelForm
from flask_bootstrap import Bootstrap
import backend as be


app = Flask(__name__)

#client = MongoClient("mongodb+srv://giacomo:12345@cluster0.8buoe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#db = client['pocenea'] 

#PDFs = db['PDFs']

c = be.loadConf()
sk = c['app']['secret_key']
app.config.from_mapping(
    SECRET_KEY=b'sk')
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
        c = be.loadConf()
        pdf=request.files['pdf']
        objecthash = be.workOnObj(pdf)

        # Prepare metadata
        metadata={}
        metadata['name'] = request.form['nome']
        metadata['filename'] = pdf.filename
        metadata['objecthash'] = objecthash
        be.upload2mongo(metadata,'PDFs')
        return render_template('uploadDone.html')
    return render_template('uploadPDF.html',form=form)

@app.route('/insertMODEL', methods=['GET', 'POST'])
def insertMODEL():
    form = InsertModelForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        c = be.loadConf()
        model=request.files['model']
        objecthash = be.workOnObj(model)

        # Prepare metadata
        metadata={}
        metadata['name'] = request.form['nome']
        metadata['filename'] = model.filename
        metadata['objecthash'] = objecthash
        be.upload2mongo(metadata,'models')
        return render_template('uploadDone.html')
    return render_template('uploadMODEL.html',form=form)






if __name__ == '__main__':
    app.run()
