#!/bin/bash
#script that sends a request to a URL passed
curl $1 -so /dev/null -w "{%http_code}"
