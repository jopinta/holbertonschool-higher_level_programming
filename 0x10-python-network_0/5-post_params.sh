#!/bin/bash
#  request that the origin server accept the entity
curl -sX "$1" POST -d "email:test@gmail.com" -d "subject:I will always be here for PLD"
