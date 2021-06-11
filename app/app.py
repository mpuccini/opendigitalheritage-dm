# app.py
#!bin/python
from flask import Flask, request, render_template
from models import InsertPubForm, InsertModelForm
from flask_bootstrap import Bootstrap
import backend as be


app = Flask(__name__)

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

@app.route('/insertPUB', methods=['GET', 'POST'])
def insertPUB():
    form = InsertPubForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
#        c = be.loadConf()
        pub=request.files['pub']
        objecthash = be.workOnObj(pub)

        # Prepare metadata
        metadata={}
        metadata['title'] = request.form['title']
        metadata['description'] = request.form['description']
        metadata['author'] = request.form['author']
        metadata['project'] = request.form['project']
        metadata['objtype'] = 'publication'
        metadata['year'] = request.form['year']
        metadata['extension'] = request.form['extension']
        metadata['filename'] = pub.filename
        metadata['objecthash'] = objecthash
        be.upload2mongo(metadata,'pubs')
        return render_template('uploadDone.html')
    return render_template('uploadPub.html',form=form)

@app.route('/insertMODEL', methods=['GET', 'POST'])
def insertMODEL():
    form = InsertModelForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
#        c = be.loadConf()
        model=request.files['model']
        objecthash = be.workOnObj(model)

        # Prepare metadata
        metadata={}
        metadata['title'] = request.form['title']
        metadata['description'] = request.form['description']
        metadata['author'] = request.form['author']
        metadata['project'] = request.form['project']
        metadata['objtype'] = '3dmodel'
        metadata['year'] = request.form['year']
        metadata['extension'] = request.form['extension']
        metadata['filename'] = model.filename
        metadata['objecthash'] = objecthash

        be.upload2mongo(metadata,'models')
        return render_template('uploadDone.html')
    return render_template('uploadModel.html',form=form)

@app.route('/getInventory',)
def getInventory():
    inventory = be.connect2mongo(be.loadConf(),'inventory')
    res = inventory.find()
    return render_template('inventory.html', result=res)



if __name__ == '__main__':
    app.run(debug=True)
