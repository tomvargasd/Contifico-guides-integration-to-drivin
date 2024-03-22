import json
import requests

def getjsondata():
    with open('api_data.json', 'r') as data_json:
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
    params = getjsondata()
    url = params['drivin']['api_path']+params['drivin']['endpoints'][0]['orders']['service']+id

    headers = {
    'X-API-Key': params['drivin']['api_key'],
    'Content-Type': 'application/json'
    }

    response = requests.request("DELETE", url, headers=headers, data={})

    if response.status_code == 200:
        return response.json()
    else:
        return "Error getting guide... \n"+str(response.json())

def delGuide(id):
    print("deleting guide...")
    params = getjsondata()
    if len(id['response'])>0:
        url = params['drivin']['api_path']+params['drivin']['endpoints'][0]['orders']['service']+id['response'][0]['code']

        headers = {
        'X-API-Key': params['drivin']['api_key'],
        'Content-Type': 'application/json'
        }
        response = requests.request("DELETE", url, headers=headers, data={})

        if response.status_code == 200:
            return response.json()
        else:
            return "Error deleting guide... \n"+str(response.json())
    else:
        return "Error deleting guide... \n"+"no guide found."

def creGuide(guide):
    print("creating guide...")
    params = getjsondata()
    url = params['drivin']['api_path']+params['drivin']['endpoints'][0]['orders']['service']+params['drivin']['endpoints'][0]['orders']['query']
    client = getContificoClient(guide['destinatario']['destinatario_id'])
    products = getContificoProducts(guide['destinatario']['detalle'])
    payload = json.dumps({}) if client == "error" else  json.dumps({
    "clients": [
        {
        "code": client['id'],
        "address": client['direccion'],
        "reference": None,
        "city": guide['destinatario']['ruta'],
        "country": "Ecuador",
        "lat": None,
        "lng": None,
        "name": client['nombre_comercial'],
        "client_name": client['nombre_comercial'],
        "client_code": None,
        "address_type": "Dirección",
        "contact_name": client['nombre_comercial'],
        "contact_phone": client['telefonos'],
        "contact_email": client['email'],
        "delivered_contact_name": client['nombre_comercial'],
        "delivered_contact_phone": client['telefonos'],
        "delivered_contact_email": client['email'],
        "service_time": None,
        "sales_zone_code": None,
        "time_windows": [],
        "tags": None,
        "orders": [
            {
            "code": guide['id'],
            "alt_code": guide['id'],
            "description": "",
            "category": "Delivery",
            "units_1": None,
            "units_2": None,
            "units_3": None,
            "position": 1,
            "delivery_date": guide['fecha_inicio'],
            "priority": 0,
            "custom_1": None,
            "custom_2": None,
            "custom_3": None,
            "custom_4": None,
            "custom_5": None,
            "supplier_code": None,
            "supplier_name": None,
            "deploy_date": None,
            "items": products,
            "pickups": []
            }
        ]
        }
    ]
    })
    headers = {
    'X-API-Key': params['drivin']['api_key'],
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print("creating Drivin guide...")
    if response.status_code == 200:
        print(response.json())
        print()
    else:
        print("error creating drivin guide: Err "+str(response.status_code))

    return response.json()

    
def getContificoProducts(products):
    data = getjsondata()
    prod = []
    for p in products:
        url = data['contifico']['api_path']+data['contifico']['endpoints'][3]['product']['service']+p['producto_id']
        headers = {
        'Authorization': data['contifico']['token']
        }
        response = requests.request("GET", url, headers=headers, data={})
        prod.append(response.json())
    print("geting product info...")
    print(prod)
    print()
    return prod


def getContificoClient(id):
    data = getjsondata()
    
    url = data['contifico']['api_path']+data['contifico']['endpoints'][2]['client']['service']+id
    headers = {
    'Authorization': data['contifico']['token']
    }
    response = requests.request("GET", url, headers=headers, data={})
    if response.status_code == 200:
        print("geting client info...")
        print(response.json())
        print()
        return response.json()
    else:
        return "error"
