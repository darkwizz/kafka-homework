#!/bin/bash

ENTITY='user'

if [ -n $1 -a "$1" = "--entity" -a -n $2 ]; then
    ENTITY=$2
fi


if [ "$ENTITY" = "user" ]; then
    curl -X POST -H "Content-Type: application/json" -d @connector-init/file-connector-sink.json localhost:8083/connectors
    curl -X POST -H "Content-Type: application/json" -d @connector-init/potentially-buying-toys-connector-sink.json localhost:8083/connectors
elif [ "$ENTITY" = "product" ]; then
    curl -X POST -H "Content-Type: application/json" -d @connector-init/products-connector-sink.json localhost:8083/connectors
fi
