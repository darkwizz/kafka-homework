#!/bin/bash


curl -X POST -H "Content-Type: application/json" -d @connector-init/file-connector-sink.json localhost:8083/connectors

curl -X POST -H "Content-Type: application/json" -d @connector-init/potentially-buying-toys-connector-sink.json localhost:8083/connectors

