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
print(res.headers) ###Parámetro X-Subject-Token es el que tiene el token, lo ideal sería automatizarlo para que se obtenga este token y pase automáticamente a "Main.py"
##con ese valor de token ya se podrían realizar solicitudes a los distintos apis de servicios de openstack como glance, entre otros de manera automática.

#Por cuestiones de tiempo, se procede con el método detallado a continuación:
###Una alternativa es la de ejecutar este script "get_token.py" para luego obtener el token del output y manualmente copiarlo y pegarlo en las solicitudes GET y POST
##que se realizan en el script "Main.py"
    
#json_data=json.load(res.headers)    
#print (json_data)
res = requests.get('http://192.168.0.80:9292/v2/images', ###puerto 9292 es del servicio Image
                    headers={'content-type': 'application/json',
                             'X-Auth-Token': 'gAAAAABhPBVrrysv85HCLKQ4sf96bQSF0T9ZXHGWk_ZRqoG9M0z74maF9QaG0i8i0MBrqX6At9JnsuICbA426zAZn3tpqZpWdUD_DFg_cs0HYVjDkgc3Dnph9-ILE8criDXu7Lwmb4m9Qfe_eIKU8pzaNgK3t8fEIIL_cH8Oev63PTejXBrnCQg'
                             },
                   )
print(res.text)