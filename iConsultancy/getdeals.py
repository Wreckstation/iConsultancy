import requests

from iConsultancy.config import config

url = f"{config['URL']}/api/3/deals"

response = requests.request("GET", url)

print(response.text)