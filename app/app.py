# app.py
#!bin/python
import logging
from flask import Flask, request, render_template
from bson.objectid import ObjectId
from pymongo import results
from models import InsertPubForm, InsertModelForm, InsertImgForm, searchForm, testForm
from functions import *

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

logging.basicConfig(level=logging.DEBUG)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insertOption')
def insertOption():
    return render_template('insertOption.html')

@app.route('/insertPUB', methods=['GET', 'POST'])
def insertPUB():
    form = InsertPubForm()
    if request.method == 'POST' and form.validate_on_submit():
        c = Config()
        pub = form.obj.data
        objecthash, extension = workOnObj(pub, c.store_type)

        # Prepare metadata
        metadata={}
        
        asset = {}
        asset['title'] = request.form['title']
        asset['description'] = request.form['description']
        asset['authorship'] = request.form['authorship']
        asset['coordinates'] = {}
        asset['coordinates']['latitude'] = None
        asset['coordinates']['longitude'] = None
        asset['license'] = request.form['license']
        metadata['asset'] = asset

        project = {}
        project['name'] = request.form['project_name']
        project['year'] = request.form['project_year']
        project['url'] = request.form['project_url']
        project['partners'] = request.form['project_partners']
        metadata['project'] = project

        objectdata = {}
        objectdata['filename'] = pub.filename
        objectdata['type'] = 'publication'
        objectdata['kind'] = request.form.get('object_kind')
        objectdata['extension'] = extension
        objectdata['hash'] = objecthash

        storedata = {}
        storedata['type'] = c.store_type

        doc = {}
        doc['metadata'] = metadata
        doc['objectdata'] = objectdata
        doc['storedata'] = storedata

        upload2mongo(doc, c.mongo_uri, c.mongo_db, 'pubs')
        return render_template('uploadDone.html')
    return render_template('uploadPub.html', form=form, obj='Publication')



@app.route('/insertIMG', methods=['GET', 'POST'])
def insertIMG():
    form = InsertImgForm()
    if request.method == 'POST' and form.validate_on_submit():
        c = Config()
        img = form.obj.data
        objecthash, extension = workOnObj(img, c.store_type)

        # Prepare metadata
        metadata={}
        
        asset = {}
        asset['title'] = request.form['title']
        asset['description'] = request.form['description']
        asset['authorship'] = request.form['authorship']
        asset['coordinates'] = {}
        coord = request.form['coordinates']
        sepcoord = coord.split(',')
        asset['coordinates']['latitude'] = sepcoord[0]
        asset['coordinates']['longitude'] = sepcoord[1]
        asset['license'] = request.form['license']
        metadata['asset'] = asset

        project = {}
        project['name'] = request.form['project_name']
        project['year'] = request.form['project_year']
        project['url'] = request.form['project_url']
        project['partners'] = request.form['project_partners']
        metadata['project'] = project

        objectdata = {}
        objectdata['filename'] = img.filename
        objectdata['type'] = 'image'
        objectdata['kind'] = request.form.get('object_kind')
        objectdata['extension'] = extension
        objectdata['hash'] = objecthash

        storedata = {}
        storedata['type'] = c.store_type

        doc = {}
        doc['metadata'] = metadata
        doc['objectdata'] = objectdata
        doc['storedata'] = storedata
        upload2mongo(doc, c.mongo_uri, c.mongo_db, 'imgs')
        return render_template('uploadDone.html')
    return render_template('uploadObj.html',form=form, obj='Image')




@app.route('/insertMODEL', methods=['GET', 'POST'])
def insertMODEL():
    form = InsertImgForm()
    if request.method == 'POST' and form.validate_on_submit():
        c = Config()
        model = form.obj.data
        objecthash, extension = workOnObj(model, c.store_type)

        # Prepare metadata
        metadata={}
        
        asset = {}
        asset['title'] = request.form['title']
        asset['description'] = request.form['description']
        asset['authorship'] = request.form['authorship']
        asset['coordinates'] = {}
        coord = request.form['coordinates']
        sepcoord = coord.split(',')
        asset['coordinates']['latitude'] = sepcoord[0]
        asset['coordinates']['longitude'] = sepcoord[1]
        asset['license'] = request.form['license']
        metadata['asset'] = asset

        project = {}
        project['name'] = request.form['project_name']
        project['year'] = request.form['project_year']
        project['url'] = request.form['project_url']
        project['partners'] = request.form['project_partners']
        metadata['project'] = project

        objectdata = {}
        objectdata['filename'] = model.filename
        objectdata['type'] = '3dmodel'
        objectdata['kind'] = request.form.get('object_kind')
        objectdata['extension'] = extension
        objectdata['hash'] = objecthash

        storedata = {}
        storedata['type'] = c.store_type

        doc = {}
        doc['metadata'] = metadata
        doc['objectdata'] = objectdata
        doc['storedata'] = storedata

        upload2mongo(doc, c.mongo_uri, c.mongo_db, 'models')
        return render_template('uploadDone.html')
    return render_template('uploadObj.html',form=form, obj='3D Model')

@app.route('/getInventory')
def getInventory():
    c = Config()
    inventory = connect2mongo(c.mongo_uri, c.mongo_db, 'inventory')
    res = inventory.find()
    return render_template('inventory.html', result=res)

@app.route('/search',methods=['GET', 'POST'])
def search():
    form = searchForm(request.form)
    coll = request.args.get('coll', None)
    obj = request.args.get('obj', None)
    if  request.method == 'POST' and form.validate_on_submit(): 
        c = Config()
        collection = connect2mongo(c.mongo_uri, c.mongo_db, coll)
        query = request.form['query']
        res = collection.find({'$text':{'$search':query}})
        if coll != 'inventory':
            return render_template('results.html', result=list(res))
        else:
            return render_template('inventory.html', result=res)
    return render_template('search.html', form=form, obj=obj)


@app.route('/getPub')
def getPub():
    c = Config()
    pubs = connect2mongo(c.mongo_uri, c.mongo_db, 'pubs')
    ID = request.args.get('ID', None)
    pub = pubs.find_one({'_id': ObjectId(ID)})
    return render_template('getPub.html', pub=pub, 
                           s3_bucket=c.aws_s3_bucket, 
                           s3_region=c.aws_s3_region, 
                           fs_host=c.fs_host)


@app.route('/getImg')
def getImg():
    c = Config()
    imgs = connect2mongo(c.mongo_uri, c.mongo_db, 'imgs')
    ID = request.args.get('ID', None)
    img = imgs.find_one({'_id': ObjectId(ID)})
    return render_template('getImg.html', img=img, 
                           s3_bucket=c.aws_s3_bucket, 
                           s3_region=c.aws_s3_region, 
                           fs_host=c.fs_host)

@app.route('/getObj')
def getObj():
    c = Config()
    objs = connect2mongo(c.mongo_uri, c.mongo_db, 'models')
    ID = request.args.get('ID', None)
    obj = objs.find_one({'_id': ObjectId(ID)})
    return render_template('getObj.html', obj=obj,
                           s3_bucket=c.aws_s3_bucket, 
                           s3_region=c.aws_s3_region, 
                           fs_host=c.fs_host)



@app.route('/testFORM',methods=['GET', 'POST'])
def testFORM():
    form = testForm()
    if  request.method == 'POST' and form.validate_on_submit():
        c = Config()
        f = form.photo.data
        #        f = request.files['photo']
        #        filename = secure_filename(f.filename)
        objecthash, extension = workOnObj(f, c.store_type)
        return render_template('testRes.html', 
                               r3=objecthash,
                               r4=extension)
    return render_template('testForm.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
