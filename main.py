import json
from ApiRequest import getRequest
from src.FilterDocs import filterDocs
from src.Drivin_Guides import createGuide, deleteGuide

# open api_data json
with open('api_data.json', 'r') as data_json:
    # load data as object
    data = json.load(data_json)

#call request and sotre in var
documentsPerDate = getRequest(
    data['contifico']['api_path'], 
    data['contifico']['endpoints'][1]['referal_guide']['service'],
    data['contifico']['endpoints'][1]['referal_guide']['query'],
    data['contifico']['token'])

nulled_documents = filterDocs("A", documentsPerDate)
new_documents = filterDocs("E", documentsPerDate)

#createGuide(new_documents)
deleteGuide(nulled_documents)

