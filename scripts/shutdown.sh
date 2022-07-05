#!/bin/bash

NG_PORT=9200
FLASK_PORT=NG_PORT + 1

echo "Finding process on port: $FLASK_PORT"
pid=$(netstat -tulnp | grep :"$FLASK_PORT" | awk '{print $7}' | cut -f1 -d"/")
echo "Process found: $pid"
# kill -9 $pid
echo "Process $pid killed"
