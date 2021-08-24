# app.py
#!bin/python
from logging import debug
from flask import Flask, request, render_template
from bson.objectid import ObjectId
from flask.config import Config
from pymongo import results
from models import searchForm, InsertPubForm, InsertModelForm, InsertImgForm
from flask_bootstrap import Bootstrap
import backend as be


app = Flask(__name__)

c = be.loadConf()
sk = c['app']['secret_key']
store_type = 'fs'
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
        pub=request.files['pub']
        objecthash, extension = be.workOnObj(pub, store_type)

        # Prepare metadata
        metadata={}
        metadata['title'] = request.form['title']
        metadata['description'] = request.form['description']
        metadata['author'] = request.form['author']
        metadata['project'] = request.form['project']
        metadata['objtype'] = 'publication'
        metadata['year'] = request.form['year']
        metadata['extension'] = extension
        metadata['filename'] = pub.filename
        metadata['objecthash'] = objecthash
        metadata['store_type'] = store_type
        be.upload2mongo(metadata,'pubs')
        return render_template('uploadDone.html')
    return render_template('uploadPub.html',form=form)

@app.route('/insertMODEL', methods=['GET', 'POST'])
def insertMODEL():
    form = InsertImgForm()
    if request.method == 'POST' and form.validate_on_submit():
        model = request.files['model']
        objecthash, extension = be.workOnObj(model, store_type)

        # Prepare metadata
        metadata={}
        metadata['title'] = request.form['title']
        metadata['description'] = request.form['description']
        metadata['author'] = request.form['author']
        metadata['project'] = request.form['project']
        metadata['year'] = request.form['year']
        metadata['license_url'] = request.form['license_url']
        metadata['extension'] = extension        
        metadata['coordinates'] = {}
        coord = request.form['coordinates']
        sepcoord = coord.split(',')
        metadata['coordinates']['latitude'] = sepcoord[0]
        metadata['coordinates']['longitude'] = sepcoord[1]

        ## Prepare paradata
        # paradata = {}
        # paradata['unitMeas'] = request.form['unitMeas'] 
        # paradata['hasSubModels'] = request.form['hasSubModels']
        # paradata['hasHotspots'] = request.form['hasHotspots']
        ## change it to paradata!!
        metadata['objtype'] = '3dmodel'
        metadata['filename'] = model.filename
        metadata['objecthash'] = objecthash
        metadata['store_type'] = store_type


        ## Create doc
        # doc = {}
        # doc['metadata'] = metadata
        # doc['paradata'] = paradata
        ## Remember to upload doc instead of metadata!!
        be.upload2mongo(metadata,'models')
        return render_template('uploadDone.html')
    return render_template('uploadObj.html',form=form, obj='3D Model')

@app.route('/insertIMG', methods=['GET', 'POST'])
def insertIMG():
    form = InsertImgForm()
    if request.method == 'POST' and form.validate_on_submit():
#        img = request.files['img']
        img = form.img.data
        objecthash, extension = be.workOnObj(img, store_type)

        # Prepare metadata
        metadata={}
        metadata['title'] = request.form['title']
        metadata['description'] = request.form['description']
        metadata['author'] = request.form['author']
        metadata['project'] = request.form['project']
        metadata['objtype'] = 'image'
        metadata['year'] = request.form['year']
        metadata['license_url'] = request.form['license_url']
        metadata['extension'] = extension
        metadata['filename'] = img.filename
        metadata['objecthash'] = objecthash
        metadata['store_type'] = store_type
        metadata['coordinates'] = {}
        coord = request.form['coordinates']
        sepcoord = coord.split(',')
        metadata['coordinates']['latitude'] = sepcoord[0]
        metadata['coordinates']['longitude'] = sepcoord[1]
        be.upload2mongo(metadata,'imgs')
        return render_template('uploadDone.html')
    return render_template('uploadObj.html',form=form, obj='Image')


@app.route('/getInventory')
def getInventory():
    inventory = be.connect2mongo(be.loadConf(),'inventory')
    res = inventory.find()
    return render_template('inventory.html', result=res)

@app.route('/searchOption')
def searchOption():
     return render_template('searchOption.html')

@app.route('/search',methods=['GET', 'POST'])
def search():
    form = searchForm(request.form)
    coll = request.args.get('coll', None)
    obj = request.args.get('obj', None)
    if  request.method == 'POST' and form.validate_on_submit(): 
        collection = be.connect2mongo(be.loadConf(), coll)
        query = request.form['query']
        res = collection.find({'$text':{'$search':query}})
        if coll=='inventory':
            return render_template('inventory.html', result=res)
        return render_template('result.html', result=res)
    return render_template('search.html', form=form, obj=obj)      

# @app.route('/searchPUB',methods=['GET', 'POST'])
# def searchPUB():
#     form = SearchPubForm(request.form)
#     if  form.validate_on_submit():  #request.method=GET o POST?
#             pubs = be.connect2mongo(be.loadConf(),'pubs')
#             metadata={}
#             metadata['title'] = request.form['title']
#             return render_template('ResultPUB.html',result=pubs.find({'title':request.form['title']}))
#     return render_template('searchPUB.html',form=form)

# @app.route('/searchIMG',methods=['GET', 'POST'])
# def searchIMG():
#     form = SearchImgForm(request.form)
#     if  form.validate_on_submit():  #request.method=GET o POST?
#             imgs = be.connect2mongo(be.loadConf(),'imgs')
#             metadata={}
#             metadata['title'] = request.form['title']
#             return render_template('ResultIMG.html',result=imgs.find({'title':request.form['title']}))
#     return render_template('searchIMG.html',form=form)

# @app.route('/searchModel',methods=['GET', 'POST'])
# def searchModel():
#     form = SearchModelForm(request.form)
#     if  form.validate_on_submit():  #request.method=GET o POST?
#             models = be.connect2mongo(be.loadConf(),'models')
#             metadata={}
#             metadata['title'] = request.form['title']
#             return render_template('ResultIMG.html',result=models.find({'title':request.form['title']}))
#     return render_template('searchModel.html',form=form)

# @app.route('/searchInventory',methods=['GET', 'POST'])
# def searchInventory():
#     form = SearchInventoryForm(request.form)
#     if  form.validate_on_submit():  #request.method=GET o POST?
#             inv = be.connect2mongo(be.loadConf(),'inventory')
#             metadata={}
#             metadata['title'] = request.form['title']
#             return render_template('inventory.html',result=inv.find({'title':request.form['title']}))
#     return render_template('searchInventory.html',form=form)

@app.route('/getImg')
def getImg():
    imgs = be.connect2mongo(be.loadConf(),'imgs')
    ID = request.args.get('ID', None)
    img = imgs.find_one({'_id': ObjectId(ID)})
    c = be.loadConf()
    return render_template('getImg.html', img=img, c=c['datastore'])

@app.route('/getObj')
def getObj():
    objs = be.connect2mongo(be.loadConf(),'models')
    ID = request.args.get('ID', None)
    obj = objs.find_one({'_id': ObjectId(ID)})
    return render_template('getObj.html', obj=obj)

if __name__ == '__main__':
    app.run(debug=True)
