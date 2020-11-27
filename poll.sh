#!/bin/bash

filename=~/.robinshare
file_time=$(stat -f %B "$filename")
current_time=$(date +%s)
if (( file_time < ( current_time - ( 60 * 60 * 23 ) ) )); then
  # $filename older than 23 hours
  $(dirname $0)
  source .env
  export MYSQL_HOST MYSQL_USER MYSQL_DATABASE MYSQL_PASSWORD MYSQL_PORT RH_USER RH_PASS
  python3 rh.py >/dev/null 2>&1
fi

touch $filename
