#!/bin/bash

NG_PORT=9200
FLASK_PORT=NG_PORT + 1
HOST="0.0.0.0"

export FLASK_APP=../back-end/wsgi.py
export FLASK_ENV=production
export FLASK_RUN_PORT=$FLASK_PORT
export FLASK_RUN_HOST=$HOST

# source ../back-end/venv/bin/activate
# flask run
echo "--- flask run ---"
pwd

cd ../front-end/sports-streams
echo "--- cd ../front-end/sports-streams ---"
pwd

echo $NG_PORT
echo $FLASK_PORT
echo $HOST
echo "---"
echo $FLASK_APP
echo $FLASK_ENV
echo $FLASK_RUN_PORT
echo $FLASK_RUN_HOST
