import requests

r = requests.get('localhost:7000')

print(r.text)