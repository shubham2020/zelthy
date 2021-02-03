#!/usr/bin/env python3

import requests 
import json

import jsonDataToSend as jds
import time
  
# defining the endpoint  
url = 'http://0.0.0.0:8000/purchase/data-upload/'
  
# payload of the entire data set
payloads = jds.DataPreparation().finalPayload()

headers = {'content-type': 'application/json'}

for payload in payloads:
  r = requests.post(url, data=json.dumps(payload), headers=headers)
  print(payload)