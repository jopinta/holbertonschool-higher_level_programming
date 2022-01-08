#!/bin/bash
# displays all HTTP methods accepted
curl -s -I "$1" | grep "Allow" | cut -d' ' -f2-
