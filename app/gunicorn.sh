#!/bin/sh

#gunicorn --chdir app wsgi:app -w 2 --threads 2 -b 0.0.0.0:5000
gunicorn app:app -w 2 --threads 2 -b 0.0.0.0:5000 -m 007
