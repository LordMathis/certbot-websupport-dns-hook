#!/bin/bash

source auth.env

python authenticator.py $CERTBOT_DOMAIN $CERTBOT_VALIDATION $KEY $SECRET
sleep 60
