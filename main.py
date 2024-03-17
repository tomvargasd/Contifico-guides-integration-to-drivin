import datetime
import json
from src.ApiRequest import getRequest
from src.FilterDocs import filterDocs

# open api_data json
with open('api_data.json', 'r') as data_json:
    # load data as object
    data = json.load(data_json)

# Obtener la fecha y hora actual
date_now = datetime.datetime.now()

# Formatear la fecha y hora actual en "dd/mm/Y"
date = date_now.strftime("%d/%m/%Y")
date = "24/01/2022" #date burned

#call request and sotre in var
documentsPerDate = getRequest(
    data['contifico']['api_path'], 
    data['contifico']['endpoints']['document_per_date']['service'],
    data['contifico']['endpoints']['document_per_date']['query']+date,
    data['contifico']['token'])

nulled_documents = filterDocs(True, documentsPerDate)

new_documents = filterDocs(False, documentsPerDate)