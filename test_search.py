from googleapiclient.discovery import build
import json, logging
my_api_key = "AIzaSyDjJQqT8xLvxZFse2zUbf7R6JnVhv2JOkc" 
my_cse_id = "189d8811d7571443d"
LOG = logging.getLogger('sw.google_search')

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

def _decode_response(json_string):
    response = json.loads(json_string)

    meta = {key: value for key, value in response.items() if key != 'items'}
    num_results = int(meta['searchInformation']['totalResults'])
    if num_results == 0:
        LOG.info("No search results.")
        LOG.info(json.dumps(response, indent=4))
        return []
    else:
        LOG.info("{} results.".format(num_results))

    for item in response['items']:
        item['meta'] = meta

    return response['items']


result = google_search("Coffee", my_api_key, my_cse_id)
#print(result)
print("=====")
pretty_result = json.dumps(result, indent=4)
print(pretty_result)

#print(_decode_response(pretty_result))