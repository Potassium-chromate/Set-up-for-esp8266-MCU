import requests
import json

url = "http://192.168.4.1/sendArray"  # Replace with the IP address of your ESP8266
array = [1, 2, 3, 4, 5]

response = requests.post(url, data=json.dumps(array))
print(response.text)
