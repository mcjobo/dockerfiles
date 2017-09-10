#!/bin/bash

# in these file we want to start the docker container of the dhcp server

docker stop jbolay-dhcp
docker rm jbolay-dhcp
docker  run -d  -p 67:67/udp --net=host --name jbolay-dhcp jbolay/dhcp /sbin/my_init 
