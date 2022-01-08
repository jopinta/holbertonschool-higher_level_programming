#!/bin/bash
# displays all HTTP methods accepted
curl -s -X "$1" OPTIONS -i

