#!/bin/bash
#download file
curl -s "$1" | grep -i Content-Length | awk '{print $2}'  
