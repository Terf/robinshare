Clone and create a `.env` file like
```
MYSQL_ROOT_PASSWORD=plasticdisneyfish
MYSQL_HOST=165.22.6.7
MYSQL_USER=main
MYSQL_DATABASE=main
MYSQL_PORT=3000
MYSQL_PASSWORD=sevenfortheseven
RH_USER=terf773
RH_PASS=webdug872
```
Run `python rh.py` to send holdings, or periodically run `poll.sh` as a cron job (`crontab -e`)
```
0 * * * * /path/to/robinshare/poll.sh
```
