#!/bin/bash
#This is another comment
[[ "$(curl -sI "$1" | awk 'NR==1')" == *"200 OK"* ]] && echo "$(curl -s "$1")"
