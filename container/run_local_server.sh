#!/bin/sh

# read command line argument into a variable called 'image'
image=$1

# run docker service on port 8080
docker run --name mylocalservice -d -p 8080:8080 --rm ${image} serve
