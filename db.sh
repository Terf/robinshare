#!/bin/bash

docker run --name rh-mysql --env-file .env -v rh-data:/var/lib/mysql --restart always -p 3000:3306 -d mysql
