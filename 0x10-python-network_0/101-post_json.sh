#!/bin/bash
#script that sends a JSON POST
curl -s -H "Content-Type: application/json" $1 -d @"$2"
