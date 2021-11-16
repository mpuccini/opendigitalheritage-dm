# *PoC* of data managment module of ENEA Open Digital Heritage ecosystem

## General info
This is the Proof of Concept of the data managment module of the ENEA Open Digital Heritage ecosystem. The PoC is a web app that is the result of the Heritage Science Internship 2021 in ENEA. This module allow to upload and get cultural heritage digital data with a search tool working with mongoDB. It is containarized to ensure portability.  
More informations on the app itself (not the containerization) are in the [Architectural document](docs/arch-doc.md).  

> this application is based on a mongoDB database storage service and a data storage service of your choice between a file system (exposed over https) or an S3 object storage (with .aws/credentials). Both database and storage are given for acquired and their installation and configuration will not be discussed in this document. Regarding the mongoDB database, this is the structure that this application expects to find:  
>  - database: heritagescience
>    - collections: inventory, imgs, pubs, models  
>
> Before proceeding with the deployment of the application, it is therefore necessary to setup these services.

## Instructions
This PoC can run in *development mode* in you local machine or deployed as containerized *production-ready* service on your server and/or on common public cloud providers.

### Get the code
First of all you need to get the code:
```
git clone https://github.com/mpuccini/opendigitalheritage-dm.git
```
and jump to its folder:
```bash
cd opendigitalheritage-dm
```

### Make some configurations
You first need to configure mongoDB connection, where to store data (File System or AWS S3) and set related setups. So, you need to copy the `app/env-sample` file into an `app/.env` file with your configuration for each variable. These will be used as environment variables (leave blanks if not used, or delete them).
```ini
APP_NAME=opendigitalheritage-dm
ENV_FILE=app/.env
MONGO_DATABASE=<yourdb>
MONGO_URI=mongodb+srv://<user>:<passwd>@<mongohost>/<yourdb>?retryWrites=true&w=majority
STORE_TYPE=s3 (or fs)
AWS_S3_BUCKET=<yourbucket>
AWS_S3_REGION=<yourS3region>
AWS_CREDENTIALS=.aws/credentials
FS_HOST=<remote/localFSost>
FS_PATH=<FSpath>
```

Once you have the `.env` file, you just need to export variables into the environment with (go inside the `app` folder first):
```bash
cd app
export $(xargs < .env)
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
#### Configuration
Add this to your server `.bashrc` or `.profile`:
```bash
export FS_PATH=<FSpath>
```
to set this variable both inside and outside container. 

#### Commands
To simplify container managment, a `Makefile` is provided. In the following are summarized all the available commands. For security reason is recommmended to use podman in a *rootless* mode. You find [here](https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md) a good guide on how to configure your podman to work rootless. 


| Action | `command` |
|:---|:---|
| Build image | `make build` |
| Run container with S3 | `make run-s3` |
| Run container with FS | `make run-fs` |
| Stop container | `make stop` |
| Start container | `make start` |
| Kill (stop & remove) container) | `make kill` |
| Clean (remove eventually dead containers and remove images)) | `make clean` |

> ### Some notes
> You may need to configure your web server to proxy pass the service on standard http/https ports.   


## To Do
 - [ ] Authentication layer
 - [X] Add map to get coordinates on upload
 - [X] Add map to results page to show objects location
 - [ ] Metadata definition (JSON-LD)
 - [X] Env variables
 - [X] Fix data storage path
 - [ ] Templates refactoring
 - [X] Full text search
 - [X] Enhance frontend
 - [ ] Add features:
   - [X] Documents viewer
   - [X] Image viewer
   - [ ] Multi image upload and view
   - [ ] Multi model upload
 - [ ] Datetime support for temporal queries 
