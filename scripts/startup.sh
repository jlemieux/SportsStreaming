#!/bin/bash

NG_PORT=9200
FLASK_PORT=$((NG_PORT + 1))
HOST="0.0.0.0"
APP_DIR="$(dirname $(dirname $(realpath $0)))"
BACKEND=$APP_DIR/back-end
FRONTEND=$APP_DIR/front-end/sports-streams

export FLASK_APP=wsgi.py
export FLASK_ENV=production
export FLASK_RUN_PORT=$FLASK_PORT
export FLASK_RUN_HOST=$HOST

cd $BACKEND
source ./venv/bin/activate
flask run &

cd $FRONTEND
pwd

echo $NG_PORT
echo $FLASK_PORT
echo $HOST
echo "---"
echo $FLASK_APP
echo $FLASK_ENV
echo $FLASK_RUN_PORT
echo $FLASK_RUN_HOST
