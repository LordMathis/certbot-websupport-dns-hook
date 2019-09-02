from sys import argv
import hmac
import hashlib
import time
import requests
import base64
import json
from datetime import datetime

certbot_auth_output = argv[1]
certbot_domain = argv[2]
apiKey = argv[3]
secret = argv[4]

method = "GET"
path = "/v1/user/self/zone/" + certbot_domain + "/record"
timestamp = int(time.time())
api = "https://rest.websupport.sk"

canonicalRequest = "%s %s %s" % (method, path, timestamp)
signature = hmac.new(secret.encode('utf-8'), canonicalRequest.encode('utf-8'), hashlib.sha1).hexdigest()

headers = {
    "Authorization": "Basic %s" % (base64.b64encode("{}:{}".format(apiKey, signature).encode('utf-8'))),
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Date": datetime.fromtimestamp(timestamp).isoformat()
}

res_dict = json.loads(certbot_auth_output)
record_id = res_dict['item']['id']

# This GET request is necessary, otherwise you'll get 403 response on the DELETE request
requests.get("%s%s" % (api, path), headers=headers).content

path = path + "/" + str(record_id)
print requests.delete("%s%s" % (api, path), headers=headers).content
