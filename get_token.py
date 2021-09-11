import requests
import json

def obtener_Token():
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
                        "id": "default"
                    },
                    "name": "admin"
                }
            }
        }
    }

    ##solicitud POST para obtener un token y poder acceder a otros apis y poder ejecutar operaciones
    res = requests.post('http://192.168.0.80:5000/v3/auth/tokens',
                        headers = {'content-type':'application/json'},
                        data=json.dumps(payload))
    h
    return print(res.headers.)