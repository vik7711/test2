#!/bin/bash

url="http://www.apple.com"
logfile="curl.log"

while true; do
  timestamp=$(date +"%Y-%m-%d %H:%M:%S")

  if curl -sSf $url >/dev/null 2>&1; then
    echo "Connection to $url successful at $timestamp"
  else
    http_status=$(curl -s -o /dev/null -w "%{http_code}" $url)
    if [[ $http_status == "404" ]]; then
      echo "Connection to $url failed with 404 error at $timestamp" >&2
    else
      echo "Connection to $url failed at $timestamp" >&2
      curl -v $url 2>&1 | tee -a $logfile >&2
    fi
  fi

  sleep 1
done
