import json
import requests
from pprint import pprint

response = requests.get('https://sandboxsdwan.cisco.com:8443/dataservice/device',
                        auth=('devnetuser','Cisco123!'),
                        verify= False)

json_data = response.json()

for device in json_data['data']:
    print(f" Nombre del Host :{device['host-name']}")
    print(f" Tipo de dispositivo :{device['device-type']}")
    print(f" Estatus: {device['status'].capitalize()}")
    print("---------------------------------------------------")
    