#!/bin/bash

APP_DIR="$(dirname $(dirname $(realpath $0)))"
BUILD_DIR=$APP_DIR/front-end/dist
TARGET_DIR=/var/www/html/sports

sudo rm -f $TARGET_DIR/*
sudo cp $BUILD_DIR/* $TARGET_DIR/
