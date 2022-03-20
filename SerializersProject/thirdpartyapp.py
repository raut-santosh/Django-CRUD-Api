# this is just third party app it can be any app which can now communicate with this api using url
import requests

URL = "http://127.0.0.1:8000/all_info"

r = requests.get(url=URL)

data = r.json()

print(data)