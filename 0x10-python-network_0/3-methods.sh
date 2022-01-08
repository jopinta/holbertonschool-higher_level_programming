#!/bin/bash
# displays all HTTP methods accepted
curl -sI "$1" OPTIONS -i

