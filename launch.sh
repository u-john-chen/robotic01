#!/bin/bash

echo "###### Start Webserver in background via 'nohup python3 ./webserv.py &' ########"
nohup python3 ./webserv.py &

echo "##### Generate some data in backgroup to ./webserv.dat ########"
i=0; while :; do echo "$i, $i, $i" >>./webserv.dat; ((i++)); sleep 0.1; done &

for N in {1..100000}; do python3 ./client.py; sleep 0.5; done

