#!/bin/bash

source auth.env

python cleanup.py $CERTBOT_AUTH_OUTPUT $CERTBOT_DOMAIN $KEY $SECRET