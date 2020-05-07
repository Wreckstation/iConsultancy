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
    # Request a dictionary of deals using the specified filters.
    payload = {}
    for field in filters:
        val = filters[field]
        if not str(val).isspace():
            payload[f'filters[{field}]'] = val
    payload[f'orders[{order}]'] = sort['sortorder']

    response = request_stuff('deals', payload)
    return response

def request_tags(search):
    # Request a dictionary of tags using a name search. Returns multiple if found.
    payload = {'search': search}
    response = request_stuff('tags', payload)
    return response

def request_scores():
    # Request a dictionary of all scores found.
    response = request_stuff('scores')
    return response

def request_stages(search):
    # Request a dictionary of deal stages using a name search. Returns multiple if found.
    payload = {'filters[title]': search}
    response = request_stuff('dealStages', payload)
    return response

def request_stuff(searchtype, payload={'':''}):
    # Request a dictionary of deal stages using a name search. Returns multiple if found.
    url = config["URL"] + searchtype
    response = s.get(url, params=payload)
    response.close() # Close connection to server
    return response

def return_score_ids(search=''):
    response = request_scores().json()
    id = -1
    for score in response['scores']:
        if score['name'] == search:
            id = score['id']
    return id

def return_ids(search, b_multiple_search=False, idtype=None, searchmethod=None):
    # method returns several codes on exit depending on state.
    # Return format is an array: [(exit code), (ids found as an array)]
    # 0 = no tags were found
    # 1 = success
    # 2 = success, but multiple ids were found and only the first was used
    # 3 = success, multiple ids returned
    response = searchmethod(search).json()
    if not response or int(response['meta']['total']) == 0:
        return [0, '']
    elif int(response['meta']['total']) >= 2:
        if not b_multiple_search:
            return [2, [response[idtype][0]['id']]]
        else:
            a = []
            for i in response[idtype]:
                a += i['id']
            return [3, a]
    else:
        return [1, [response[idtype][0]['id']]]

def return_tag_ids(search, b_multiple_tag_search = False):
    return return_ids(search, b_multiple_tag_search, 'tags', request_tags)

def return_stage_id(search):
    return return_ids(search, False, 'dealStages', request_stages)

def request(filters, sort, b_output_type = True, fn = None, mt = False):
    # Prepare tag id search by converting name to ids
    req_filters = filters
    req_filters['tag'] = ''
    tags = ['']
    tag_response_code = -1
    notices = ''
    # score API request formatting
    if not filters['score_name'].isspace():
        score_id = return_score_ids(filters['score_name'])
        for x in ['score_greater_than', 'score_less_than', 'score']:
            if x in req_filters:
                val = req_filters[x]
                req_filters[x] = f'{score_id}:{val}'
        del req_filters['score_name']
    # Use API to change stage name search to ID
    if not filters['stage'].isspace():
        stage_id = return_stage_id(filters['stage'])[1]
        req_filters['stage'] = stage_id
    # tag search
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
        del req_filters['tags']
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
        result.to_csv(fn)
        return [result.to_csv(), notices]

def tag_request(filters, b_output_type = True, fn = None, mt = False):
    # This is for debug testing purposes
    tag_response = return_tag_ids(filters['tags'], mt)
    tag_response_code = tag_response[0]
    tags = tag_response[1]
    return tag_response[0]
