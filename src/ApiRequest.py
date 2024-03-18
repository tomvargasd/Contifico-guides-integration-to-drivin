import json
import requests

def getjsondata():
    with open('../api_data.json', 'r') as data_json:
        data = json.load(data_json)
    return data

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

def getDrivId(id):
    print("get")

def delGuide(id):
    print("del")

def creGuide(data):
    jsonData = getjsondata()
    for guide in data:
        scen_token = ceateScenario(guide, jsonData['drivin']['api_path'], jsonData['drivin']['endpoints'][0]['scenarios']['service'], jsonData['drivin']['endpoints'][0]['scenarios']['query'], jsonData['drivin']['api_key'])
        if scen_token['success']:
            scenarioToken = scen_token['response']['scenario_token']
            

def getContificoClient(id):
    data = getjsondata()
    
    url = data['contifico']['endpoints']['client']['service']+id
    headers = {
    'Authorization': data['contifico']['token']
    }
    response = requests.request("GET", url, headers=headers, data={})
    if response.status_code == 200:
        return response.json()
    else:
        return "error"
    

def ceateScenario(data, path, endpoint, query, token):
    cli = getContificoClient(data['destinatario']['destinatario_id'])
    clientArray = []
    if cli != "error":
        clientArray = [
            {
            "address": data['destinatario']['direccion'],
            "reference": cli['direccion'],
            "city": "Ecuador",
            "country": data['destinatario']['ruta'],
            "name": cli['nombre_comercial'],
            "client_name": cli['nombre_comercial'],
            "address_type": "",
            "contact_name": cli['nombre_comercial'],
            "contact_phone": cli['telefonos'],
            "contact_email": cli['email'],
            "time_windows": [],
            "tags": [],
            "orders": []
            }
        ]
    payload = json.dumps({
    "description": "Escenario de "+data['descripcion'],
    "date": data['fecha_emision'],
    "schema_name": "NO DEPOSIT",
    "clients": clientArray
    })
    headers = {
    'X-API-Key': '{{'+token+'}}',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", path+endpoint+query, headers=headers, data=payload)
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        return {"success": False}
