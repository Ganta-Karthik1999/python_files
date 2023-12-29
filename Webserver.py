import requests

r = requests.get('https://httpbin.org/get')
print(r.status_code)
# with open('img.png','wb') as f:
#     f.write(r.content)


