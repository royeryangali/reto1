import requests
import json

payload = { ###estos valores están detallados en el archivo admin-openrc.sh que está en la ruta /etc/whitecloud (que es el paso de cargar credenciales)
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
print(res.headers) ###Parámetro X-Subject-Token es el que tiene el token, lo ideal sería automatizarlo para que se obtenga solo este token y pase a "Main.py"
##con ese valor de token ya se podrían realizar solicitudes a los distintos apis de servicios de openstack como glance, entre otros.

    
    