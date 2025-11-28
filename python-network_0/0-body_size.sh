#!/bin/bash
# display Content-Length
curl -sL "$1" | wc -c