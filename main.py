import datetime
import requests
import json

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

# ----------------------------------------------------------------------------------------------------- START POINT
    
# open api_data json
with open('api_data.json', 'r') as data_json:
    # load data as object
    data = json.load(data_json)

# Obtener la fecha y hora actual
date_now = datetime.datetime.now()

# Formatear la fecha y hora actual en "dd/mm/Y"
date = date_now.strftime("%d/%m/%Y")
      
#date = "24/01/2022" #date burned

#call request and sotre in var
documentsPerDate = getRequest(
    data['contifico']['api_path'], 
    data['contifico']['endpoints']['document_per_date']['service'],
    data['contifico']['endpoints']['document_per_date']['query']+date,
    data['contifico']['token'])

print(documentsPerDate) #TODO: code to sync