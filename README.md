# Certbot Manual Hooks For WebSupport DNS

Get Letsencrypt wildcard certificate for your domain managed at [websupport.sk](websupport.sk)

## Requirements

* Python 2.7
* [requests](https://2.python-requests.org/en/master/user/install/#install)

## Usage

* Edit `auth.env` with the key and secret that you generated at websupport
* Run certbot
  ```
  sudo certbot certonly --manual 
                        --preferred-challenges=dns
                        --manual-auth-hook ./authenticator.sh
                        --manual-cleanup-hook ./cleanup.sh
                        --manual-public-ip-logging-ok
                        -d "*.example.com
  ```
