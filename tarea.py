import requests 
from pprint import pprint

response = requests.post('https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token', auth=('devnetuser','Cisco123!'))
payload=response.json()
pprint(payload)