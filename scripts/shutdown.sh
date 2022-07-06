#!/bin/bash

NG_PORT=9200
FLASK_PORT=$((NG_PORT + 1))

echo "Finding process on port: $FLASK_PORT"
pid=$(netstat -tulnp | grep ":$FLASK_PORT" | awk '{print $7}' | cut -f1 -d"/")
echo "Process found: $pid"

re='^[0-9]+$'
if [[ $pid =~ $re ]]
then
    echo "Killing flask server..."
    kill -9 $pid
    echo "Killed."
fi
sudo shutdown -h now

