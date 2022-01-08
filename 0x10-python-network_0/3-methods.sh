#!/bin/bash
# displays all HTTP methods accepted
cur2l -sI "$1"| grep "ALLOW" | awk '{print $2}'

