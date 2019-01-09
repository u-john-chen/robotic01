import json
import requests

r = requests.get('http://100.115.92.199:8000/coordinator')
data = r.json()

t = data['coordinator']['t']
x = data['coordinator']['x']
y = data['coordinator']['y']

print(t, x, y)

