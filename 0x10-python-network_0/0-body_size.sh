#!/bin/bash
#Displaying size of http response header in bytes
echo "$(curl -sI "$1" | grep "Content-Length: " | awk '{print $2}')"
