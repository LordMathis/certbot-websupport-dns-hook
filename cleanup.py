from sys import argv
import hmac
import hashlib
import time
import requests
import base64
import json
from datetime import datetime

certbot_auth_output = argv[1]
apiKey = argv[2]
secret = argv[3]

method = "GET"
path = "/v1/user/self/zone/namesny.com/record"
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

res = requests.get("%s%s" % (api, path), headers=headers).content
res_dict = json.loads(res)

record_id = None

with open('tmp.json') as json_data:
    d = json.load(json_data)
    print d

    for item in res_dict['items']:
        if item['name'] == d['name'] and item['type'] == 'TXT' and item['content'] == d['content']:
            record_id = item['id']

path = path + "/" + str(record_id)
print requests.delete("%s%s" % (api, path), headers=headers).content
