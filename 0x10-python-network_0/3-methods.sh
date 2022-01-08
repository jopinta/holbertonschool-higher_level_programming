#!/bin/bash
# displays all HTTP methods accepted
cur2l -sI "$1" X-Content-Type-Options: nosniff | grep "ALLOW"
