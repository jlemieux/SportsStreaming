#!/bin/bash

FLASK_PORT=9200
HOST="0.0.0.0"
APP_DIR="$(dirname $(dirname $(realpath $0)))"
BACKEND=$APP_DIR/back-end

export FLASK_APP=wsgi.py
export FLASK_ENV=production
export FLASK_RUN_PORT=$FLASK_PORT
export FLASK_RUN_HOST=$HOST

cd $BACKEND
source ./venv/bin/activate
flask run &
