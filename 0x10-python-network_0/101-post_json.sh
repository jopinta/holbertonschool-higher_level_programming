#!/bin/bash
#script that sends a JSON POST
curl -Hs "Content-Type: application/json" $1 -d @"$2"
