import requests
import json

payload = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "admin",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "vC3kwt5Yhkd4rewtRFF365TbHT8TuYo1lFaTbH4x"}
            }
        },
        "scope": {
            "project": {
                "domain": {
                    "id": "Default"
                },
                "name": "admin"
            }
        }
    }
}

##solicitud POST para obtener un token y poder acceder a otros apis
res = requests.post('http://192.168.0.80:5000/v3/auth/tokens',
                    headers = {'content-type':'application/json'},
                    data=json.dumps(payload))

print(res.headers)