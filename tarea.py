import requests 
from pprint import pprint

response = requests.post('https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token', auth=('devnetuser','Cisco123!'))
payload=response.json()
pprint(payload)

# Segunda parte del enunciado
token = payload['Token']
response = requests.get('https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',headers={"X-Auth-Token":token})
payload2 = response.json()
pprint(payload2)