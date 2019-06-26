#!/bin/sh

source auth.env

curl "https://rest.websupport.sk/v1/user/self/zone/$CERTBOT_DOMAIN/record" -H "Content-Type: application/json" \
 -X POST -d '{"type":"TXT","name":"@","content": '$CERTBOT_VALIDATION',"ttl": 600}' -u $KEY:$SECRET

