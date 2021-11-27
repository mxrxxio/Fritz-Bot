import time
from dotenv import load_dotenv
import os
import requests

load_dotenv()

# vars
http_method = "GET"
bitso_key = os.getenv('API_KEY')
request_path = "/v3/balance/"
parameters = {}

nonce =  str(int(round(time.time() * 1000)))

# Build the auth header
auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)

# Send request
if (http_method == "GET"):
  response = requests.get("https://api.bitso.com" + request_path, headers={"Authorization": auth_header})