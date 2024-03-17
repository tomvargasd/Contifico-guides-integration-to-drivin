import requests

def getRequest(path, endpoint, query, token):

    #authorization
    headers = { 'Authorization': token }

    #execution query
    response = requests.request("GET", path+endpoint+query, headers=headers, data={})

    #response validation
    if response.status_code == 200:
        return response.json()
    else:
        return [{"error": "Status code "+str(response.status_code)}]