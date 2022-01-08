#!/bin/bash
# displays all HTTP methods accepted
curl -s "$1" OPTIONS -i

