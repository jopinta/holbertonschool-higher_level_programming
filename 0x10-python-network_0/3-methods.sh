#!/bin/bash
# displays all HTTP methods accepted
curl -s X OPTIONS "$1" -i

