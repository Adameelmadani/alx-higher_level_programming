#!/bin/bash
#Displaying size of http response header in bytes
line=$(curl -sI "$1" | grep "Content-Length: ")
line="${line:16}"
echo "$line"
