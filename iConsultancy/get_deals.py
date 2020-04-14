import requests
from requests.auth import HTTPBasicAuth

from iConsultancy.config import config

# Get requests from the server
headers = {'Api-Token': config["KEY"]}
s = requests.Session()
s.headers.update(headers)

def request(filters):
    payload = {'filters[search_field]': filters['search_field'],
               'filters[search]': filters['search'],
               'filters[status]': filters['status'],
               'filters[stage]': filters['stage'],
               'filters[owner]': filters['owner'],
               'filters[tag]': filters['tag'],
               'filters[tasktype]': filters['tasktype'],
               'filters[nextdate_range]': filters['nextdate_range']
               }
    url = config["URL"] + "deals"
    response = s.get(url, params=payload)
    response.close() # Close connection to server
    return response
