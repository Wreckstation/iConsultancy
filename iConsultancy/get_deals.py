import requests
from requests.auth import HTTPBasicAuth

import iConsultancy.to_csv as to_csv
from iConsultancy.config import config

# Prepare session and headers
headers = {'Api-Token': config["KEY"]}
s = requests.Session()
s.headers.update(headers)

def request_deals(filters, sort):
    order = sort['sortby'] 
    # Request a dictionary of deals using the specified filters and sort order.
    payload = {'filters[search_field]': filters['search_field'],
               'filters[search]': filters['search'],
               'filters[status]': filters['status'],
               'filters[stage]': filters['stage'],
               'filters[owner]': filters['owner'],
               'filters[tag]': filters['tag'],
               'filters[tasktype]': filters['tasktype'],
               'filters[nextdate_range]': filters['nextdate_range'],
               f'orders[{order}]': sort['sortorder']
               }  
    url = config["URL"] + "deals"
    response = s.get(url, params=payload)
    response.close() # Close connection to server
    return response

def request_tags(search):
    # Request a dictionary of tags using a name search. Returns multiple if found.
    payload = {'search': search}
    url = config["URL"] + "tags"
    response = s.get(url, params=payload)
    response.close() # Close connection to server
    return response

def return_tag_ids(search, b_multiple_tag_search = False):
    # method returns several codes on exit depending on state.
    # Return format is an array: [(exit code), (tag ids found as an array)]
    # 0 = no tags were found
    # 1 = success
    # 2 = success, but multiple tags were found and only the first was used
    # 3 = success, multiple tags returned
    response = request_tags(search).json()
    if not response or int(response['meta']['total']) == 0:
        return [0, '']
    elif int(response['meta']['total']) >= 2:
        if not b_multiple_tag_search:
            return [2, [response['tags'][0]['id']]]
        else:
            a = []
            for i in response['tags']:
                a += i['id']
            return [3, a]
    else:
        return [1, [response['tags'][0]['id']]]

def request(filters, sort, b_output_type = True, fn = None, mt = False):
    # Prepare tag id search by converting name to ids
    req_filters = filters
    req_filters['tag'] = ''
    tags = ['']
    tag_response_code = -1
    notices = ''
    if filters['tags'] != '':
        tag_response = return_tag_ids(filters['tags'], mt)
        tag_response_code = tag_response[0]
        tags = tag_response[1]
        if tag_response_code == 0:
            notices += 'There weren\'t any tags that match your search. It was ignored.\n\n'
        elif tag_response_code == 2:
            notices += 'There was more than one tag that was returned, but deals that only match the first one were returned.\n\n'
        elif tag_response_code == 3:
            notices += 'There was more than one tag that was similar to your query, and all matches were returned.\n\n'
        result = None
        for tag in tags: # If searching by multiple tags, search all and concat into one df
            req_filters['tag'] = tag
            if result is None:
                result = to_csv.json_to_df(request_deals(req_filters, sort).json())
            else:
                result += to_csv.json_to_df(request_deals(req_filters, sort).json())
    else:
        result = to_csv.json_to_df(request_deals(req_filters, sort).json())
    # Return values based on output type: True for JSON, False for CSV
    if b_output_type:
        return [result.to_json(), notices]
    else:
        return [result.to_csv(fn), notices]

def tag_request(filters, b_output_type = True, fn = None, mt = False):
    # This is for debug testing purposes
    tag_response = return_tag_ids(filters['tags'], mt)
    tag_response_code = tag_response[0]
    tags = tag_response[1]
    return tag_response[0]