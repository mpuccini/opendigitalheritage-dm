# *PoC* of data managment module of ENEA Open Digital Twins ecosystem

## General info
This is the Proof of Concept of the data managment module of the ENEA Open Digital Twins ecosystem. The PoC is a web app that is the result of the Heritage Science Internship 2021 in ENEA. This module allow to upload and get cultural heritage digital data with a search tool working with mongoDB. It is containarized to ensure portability.  
More informations on the app itself (not the containerization) are in the [Architectural document](docs/arch-doc.md).

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
cd app/
python app.py
```
You may also want to test loaclly the wsgi server with gunicorn. In this case you just need to:
```bash
cd app/
bash gunicorn.sh
```

### Run as container (Producion)
To simplify container managment, a `Makefile` is provided. In the following are summarized all the available commands. For security reason is recommmended to use podman in a *rootless* mode. You find [here](https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md) a good guide on how to configure your podman to work rootless. 

#### Configuration
In the `config.ini` set the `path` variable of `[datastore]` field to `/store/':  
```bash
...
[datastore]
	path = /store/
...
```

And then set your local path into the Makefile in the `run` rule:  
```cpp
@docker run --detach -p 5000:5000 -v </your/path>:/store:Z $(app_name)
```


#### Commands

| Action | `command` |
|:---|:---|
| Build image | `make build` |
| Run container | `make run` |
| Stop container | `make stop` |
| Start container | `make start` |
| Kill (stop & remove) container) | `make kill` |
| Clean (remove eventually dead containers and remove images)) | `make clean` |

> ### Some notes
> You may need to configure your web server to proxy pass the service on standard http/https ports.   


## To Do
 - [x] Add map to get coordinates on upload
 - [X] Add map to results page to show objects location
 - [ ] Metadata definition (JSON-LD)
 - [ ] Env variables
 - [ ] Fix data storage path
 - [ ] Templates refactoring
 - [ ] Full text search
 - [ ] Enhance frontend
 - [ ] Add features:
   - [ ] Documents viewer
   - [ ] Image viewer
   - [ ] Multi image upload and view
   - [ ] Multi model upload
