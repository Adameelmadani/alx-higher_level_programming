#!/bin/bash
#This is another comment
[[ "$(curl -s -w "%{http_code}" "$1")" == *"200"* ]] && echo -n "$(curl -s "$1")"
