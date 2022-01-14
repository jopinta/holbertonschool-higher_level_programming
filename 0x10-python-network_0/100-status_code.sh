#!/bin/bash
#script that sends a request to a URL passed
curl '$1' -s -o -w /dev/null "{%http_code}"
