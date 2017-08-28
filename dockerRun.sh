#!/bin/sh
echo killing all docker instances
docker kill $(docker ps -q)
echo removing all docker containers
docker rm $(docker ps -a -q)
echo building dejavu
docker build -t dejavu .
echo running dejavu
docker run -p 4000:80 dejavu
