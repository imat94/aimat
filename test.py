import requests


ok = requests.get('https://raw.githubusercontent.com/imat94/aimat/main/ok.json').json()

print(ok)