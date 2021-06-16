# *PoC* of data managment module of ENEA Open Digital Twins ecosystem

## General info
This is the Proof of Concept of the data managment module of the ENEA Open Digital Twins ecosystem. The PoC is a web app that is the result of the Heritage Science Internship 2021 in ENEA. This module allow to upload and get cultural heritage digital data with a search tool working with mongoDB. It is containarized to ensure portability.  
More informations on the app itself (not the containerization) are in the [Architectural document](arch-doc.md).

## Instructions
This PoC can run in *development mode* in you local machine or deployed as containerized *production-ready* service on your server and/or on common public cloud providers.

### Get the code
First of all you need to get the code:
```
git clone https://github.com/mpuccini/poc-eneahs.git
```
and jump to its folder:
```bash
cd poc-eneahs
```

### Make some configurations
You first need to configure mognoDB connection, where to store data and define an app key.
```ini
[mongo]
host = <mongos-hosts> 
port = 27017
user = <user-name>
pwd = <user-password>
db = <authentication-database>

[datastore]
path = <data-storage-path>

[app]
secret_key=<your-secret_key>
```

### Start for development
To start the app to develop, you first need to create your python environment. You can do this in different ways, here are showed the virtualenv way. Just create the virtualenv (assuming you have python 3.X) and activate it:
```bash
python3 -m venv <your-virtual-env>
source <your-virtual-env>/bin/activate
```
Then install requirements:
```bash
pip install -r requirements
```
Now you're ready to start the app just with:
```bash
python app/app.py
```
You may also want to test loaclly the wsgi server with gunicorn. In this case you just need to:
```bash
bash app/gunicorn.sh
```

### Run as container
To simplify container managment, a `Makefile` is provided. In the following are summarized all the available commands[^1].
Build image:
```
(sudo) make build
```
Run container:
```
(sudo) make run
```
Stop container:
```
(sudo) make stop
```
Start container:
```
(sudo) make start
```
Kill (stop & remove) container:
```
(sudo) make kill
```
Clean (remove eventually dead containers and remove images):
```
(sudo) make clean
```

[^1]:
A docker engine is assumed to be running. If you have podman instead, just create an alias:
```bash
alias docker=podman
```
