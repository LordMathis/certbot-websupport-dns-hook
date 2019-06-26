#!/bin/sh

source auth.env

ID=`echo $CERTBOT_AUTH_OUTPUT > jq '.item.id'`
DOMAIN_NAME=`echo $CERTBOT_AUTH_OUTPUT0 > jq '.item.zone.name'`

curl "https://rest.websupport.sk/v1/user/self/zone/:domain_name/record/" -X DELETE -u $KEY:$SECRET