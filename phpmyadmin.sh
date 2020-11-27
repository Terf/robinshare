#!/bin/bash

docker run --name myadmin --restart always -d --link rh-mysql:db -p 1997:80 phpmyadmin/phpmyadmin
