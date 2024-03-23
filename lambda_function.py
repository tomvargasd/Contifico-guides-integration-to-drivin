import json
from datetime import datetime
from ApiRequest import getRequest
from src.FilterDocs import filterDocs
from src.Drivin_Guides import createGuide, deleteGuide

def lambda_handler(event, context):
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
    fecha_actual = datetime.now()
    date = fecha_actual.strftime("%d/%m/%Y")
    
    nulled_documents = filterDocs("A", documentsPerDate, date)
    new_documents = filterDocs("E", documentsPerDate, date)
    
    createdGuides = createGuide(new_documents)
    deletedGuides = deleteGuide(nulled_documents)
    return {
        'statusCode': 200,
        'body': json.dumps({
            "Driv.in guides created": createdGuides,
            "Driv.in guides deleted": deletedGuides,
            "Date_syncronization": date
        })
    }
