#!/bin/bash

# in these file we want to start the docker container
#--hostname=pdc --dns=<localhost>

docker stop jbolay-pdc
docker rm jbolay-pdc
docker run -d --name=jbolay-pdc  -p 53:53 -p 53:53/udp -p 88:88 -p 88:88/udp -p 135:135 -p 137-138:137-138/udp -p 139:139 -p 389:389 -p 389:389/udp -p 445:445 -p 464:464 -p 464:464/udp -p 636:636 -p 1024-1044:1024-1044 -p 3268-3269:3268-3269   --hostname=pdc --dns=127.0.0.1 jbolay/pdc /sbin/my_init 
