#!/bin/bash

APP_DIR="$(dirname $(dirname $(realpath $0)))"
ADDONS_SOURCE=$APP_DIR/mitm/custom-addons
ADDONS_TARGET=/home/pi/.mitmproxy/custom-addons
CONFIG_SOURCE=$APP_DIR/mitm/config.yml
CONFIG_TARGET=/home/pi/.mitmproxy/config.yml

rm -rf $ADDONS_TARGET/*
cp $ADDONS_SOURCE/*.py $ADDONS_TARGET/

cp $CONFIG_SOURCE $CONFIG_TARGET
