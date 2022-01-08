#!/bin/bash
# displays all HTTP methods accepted
curl -sI "$1"| grep "ALLOW" | awk '{print $2}'

