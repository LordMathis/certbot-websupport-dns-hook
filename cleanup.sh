#!/bin/bash

source auth.env

python cleanup.py $CERTBOT_AUTH_OUTPUT $KEY $SECRET
rm tmp.json
