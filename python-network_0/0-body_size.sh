#!/bin/bash
# display Content-Length
curl -s "http://$1" | wc -c
