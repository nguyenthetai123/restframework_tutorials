import json
import requests
data={
    'name':'adsa',
    'roll':101,
    'city':'sdas'
}


URL='http://127.0.0.1:8000/api/create'


json_data = json.dumps(data)
r= requests.post(url=URL,data=json_data)


