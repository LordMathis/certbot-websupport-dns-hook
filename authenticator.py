from sys import argv
import hmac
import hashlib
import time
import requests
import base64
import json
from datetime import datetime

certbot_domain = argv[1]
certbot_validation = argv[2]
apiKey = argv[3]
secret = argv[4]

method = "POST"
path = "/v1/user/self/zone/{}/record".format(certbot_domain)
timestamp = int(time.time())
api = "https://rest.websupport.sk"

canonicalRequest = "{} {} {}".format(method, path, timestamp)
signature = hmac.new(secret.encode('utf-8'), canonicalRequest.encode('utf-8'), hashlib.sha1).hexdigest()
credentials = base64.b64encode("{}:{}".format(apiKey, signature).encode('utf-8'))

headers = {
    "Authorization": "Basic {}".format((credentials).decode('utf-8')),
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Date": datetime.fromtimestamp(timestamp).isoformat()
}

data = {
    "type": "TXT",
    "name": "_acme-challenge", 
    "content": certbot_validation
}

print(requests.post("{}{}".format(api, path), headers=headers, data=json.dumps(data)).text)
