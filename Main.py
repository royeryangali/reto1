import argparse
import os
import sys
import subprocess
import openstack
import requests
import json
from openstack import image
from openstack.config import loader
from openstack import connection
from subprocess import call


##########################################################INICIALIZACIÓN#########################################
# Para tener los logs en el archivo "LogsDeOpenStack"
openstack.enable_logging(True, path="LogsDeOpenstack.log", stream=sys.stdout)

# Se realiza la conexión a la API openstack mediante el uso del archivo clouds.yaml que ha sido descargado. Por defecto, se realizará la búsqueda en el mismo path del proyecto:
conn = openstack.connect(cloud="openstack")
##########################################################FIN INICIALIZACIÓN#########################################

##Crear un txt para guardar las salidas que nos interesan:

###
def menu():
    os.system('clear')
    print("ACTIVIDADES LABORATORIO WHITESTACK")
    print("1. Actividad 1")
    print("2. Actividad 2")
    print("3. Actividad 3")
    print("4. Actividad 4")
    print("5. Actividad 5")
    print("6. Actividad 6")

while True:
    
    menu()
    actividad = input("Seleccione el número de actividad a elegir: ")

    if actividad=="1":
        f = open("1OutputAct.txt","w")
        #####INICIO ACTIVIDAD 1#####
        # Listamos las instancias que están creadas:
        f.write("Lista de instancias creadas:\n")
        for server in conn.compute.servers(): 
            print(server.to_dict())           
            print(server.name)
            f.write("Name: "+ server.name)
            f.write("  Hostname: " + server.hostname)
            f.write("  Hostname: " + server.hypervisor_hostname)             
            f.write("\n")        

        # Listamos las imágenes disponibles:
        f.write("Lista de imágenes disponibles:\n")
        for image in conn.compute.images():
            print(image.name)
            f.write(image.name)
            f.write("\n")
        ###Método alternativo para mostrar datos más específicos de las imágenes en formato JSON - GET
        res = requests.get('http://192.168.0.80:9292/v2/images', ###puerto 9292 es del servicio Image
                    headers={'content-type': 'application/json',
                             'X-Auth-Token': 'gAAAAABhPBVrrysv85HCLKQ4sf96bQSF0T9ZXHGWk_ZRqoG9M0z74maF9QaG0i8i0MBrqX6At9JnsuICbA426zAZn3tpqZpWdUD_DFg_cs0HYVjDkgc3Dnph9-ILE8criDXu7Lwmb4m9Qfe_eIKU8pzaNgK3t8fEIIL_cH8Oev63PTejXBrnCQg'
                             },
                   )
        print(res.text)

        # Listamos los flavors disponibles:
        f.write("Lista de flavors disponibles:\n")
        for flavor in conn.compute.flavors():
            print(flavor.name)
            f.write(flavor.name)
            f.write("\n")

        ###Método alternativo para mostrar datos más específicos de flavors en formato JSON - GET
        res = requests.get('http://192.168.0.80:8774/v2.1/flavors', ###puerto 8774 es del servicio compute_legacy
                    headers={'content-type': 'application/json',
                             'X-Auth-Token': 'gAAAAABhPBVrrysv85HCLKQ4sf96bQSF0T9ZXHGWk_ZRqoG9M0z74maF9QaG0i8i0MBrqX6At9JnsuICbA426zAZn3tpqZpWdUD_DFg_cs0HYVjDkgc3Dnph9-ILE8criDXu7Lwmb4m9Qfe_eIKU8pzaNgK3t8fEIIL_cH8Oev63PTejXBrnCQg'
                             },
                   )
        print(res.text)
        #####FIN ACTIVIDAD 1#####
        f.close()
        break

    elif actividad=="2":
        g = open("2OutputAct.txt","w")
        #####INICIO ACTIVIDAD 2#####        
        os.system('openstack server list')        
        #####FIN ACTIVIDAD 2#####
        g.write("Credenciales de admin cargadas.\n")
        g.close()
        break
    elif actividad=="3":
        #####INICIO ACTIVIDAD 3#####
        #crear red privada net-1 - POST
        payload= {
            "network": {
                "name": "net-1",
                "": "",
                "": "", 
                "networks": [{
                    "uuid": "66d2d553-1a09-4be9-ad93-5f43c3a0e20d"
                }]
            }
        }
        res = requests.post('http://192.168.0.80:9696/v2.0/networks', ###puerto 8774 es del servicio Compute
                        headers={'content-type': 'application/json',
                                'X-Auth-Token': 'gAAAAABhPBVrrysv85HCLKQ4sf96bQSF0T9ZXHGWk_ZRqoG9M0z74maF9QaG0i8i0MBrqX6At9JnsuICbA426zAZn3tpqZpWdUD_DFg_cs0HYVjDkgc3Dnph9-ILE8criDXu7Lwmb4m9Qfe_eIKU8pzaNgK3t8fEIIL_cH8Oev63PTejXBrnCQg',
                                    },
                            data=json.dumps(payload)
                        )
        print(res.text)

        #crear red privada net-2 - POST

        #listas redes creadas y subredes GET
        res= requests.get("http://192.168.0.80:9696/v2.0/networks", ###puerto 9696 es del servicio Network
                     headers={'content-type': 'application/json',
                             'X-Auth-Token': 'gAAAAABhPBVrrysv85HCLKQ4sf96bQSF0T9ZXHGWk_ZRqoG9M0z74maF9QaG0i8i0MBrqX6At9JnsuICbA426zAZn3tpqZpWdUD_DFg_cs0HYVjDkgc3Dnph9-ILE8criDXu7Lwmb4m9Qfe_eIKU8pzaNgK3t8fEIIL_cH8Oev63PTejXBrnCQg'
                             },
                  )
        print(res.text)
        #####FIN ACTIVIDAD 3#####
        break
    elif actividad=="4":
        #####INICIO ACTIVIDAD 4#####
        #crear máquina virtual vm-1, m1.tiny, net-1, cirros - POST
        payload= {
            "server": {
                "name": "vm-1",
                "imageRef": "51b7f32a-0fc5-410e-9028-e34c3e910891",
                "flavorRef": "m1.tiny", #http://192.168.0.80:8774/v2.1/flavors/m1.tiny
                "networks": [{
                    "uuid": "66d2d553-1a09-4be9-ad93-5f43c3a0e20d"
                }]
            }
        }
        res = requests.post('http://192.168.0.80:8774/v2.1/servers', ###puerto 8774 es del servicio Compute
                        headers={'content-type': 'application/json',
                                'X-Auth-Token': 'gAAAAABhPBVrrysv85HCLKQ4sf96bQSF0T9ZXHGWk_ZRqoG9M0z74maF9QaG0i8i0MBrqX6At9JnsuICbA426zAZn3tpqZpWdUD_DFg_cs0HYVjDkgc3Dnph9-ILE8criDXu7Lwmb4m9Qfe_eIKU8pzaNgK3t8fEIIL_cH8Oev63PTejXBrnCQg',
                                    },
                            data=json.dumps(payload)
                        )
        print(res.text)


        #crear máquina virtual vm-2, m1.tiny, net-2, cirros - POST
        payload= {
                    "server": {
                        "name": "vm-2",
                        "imageRef": "51b7f32a-0fc5-410e-9028-e34c3e910891",
                        "flavorRef": "m1.tiny", #http://192.168.0.80:8774/v2.1/flavors/m1.tiny
                        "networks": [{
                            "uuid": "66d2d553-1a09-4be9-ad93-5f43c3a0e20d"
                        }]
                    }
                }
        res = requests.post('http://192.168.0.80:8774/v2.1/servers', ###puerto 8774 es del servicio Compute
                                headers={'content-type': 'application/json',
                                        'X-Auth-Token': 'gAAAAABhPBVrrysv85HCLKQ4sf96bQSF0T9ZXHGWk_ZRqoG9M0z74maF9QaG0i8i0MBrqX6At9JnsuICbA426zAZn3tpqZpWdUD_DFg_cs0HYVjDkgc3Dnph9-ILE8criDXu7Lwmb4m9Qfe_eIKU8pzaNgK3t8fEIIL_cH8Oev63PTejXBrnCQg',
                                            },
                                    data=json.dumps(payload)
                                )
        print(res.text)


        #####FIN ACTIVIDAD 4#####
        break
    elif actividad=="5":
        #####INICIO ACTIVIDAD 5#####
        #crear router POST
        payload= {
            "routers": {
                "name": "router-1",
                "": "",
                "": "", 
                "networks": [{
                    "uuid": "66d2d553-1a09-4be9-ad93-5f43c3a0e20d"
                }]
            }
        }
        res = requests.post('http://192.168.0.80:9696/v2.0/routers', ###puerto 8774 es del servicio Compute
                        headers={'content-type': 'application/json',
                                'X-Auth-Token': 'gAAAAABhPBVrrysv85HCLKQ4sf96bQSF0T9ZXHGWk_ZRqoG9M0z74maF9QaG0i8i0MBrqX6At9JnsuICbA426zAZn3tpqZpWdUD_DFg_cs0HYVjDkgc3Dnph9-ILE8criDXu7Lwmb4m9Qfe_eIKU8pzaNgK3t8fEIIL_cH8Oev63PTejXBrnCQg',
                                    },
                            data=json.dumps(payload)
                        )
        print(res.text)
        #asociar interfaz a subnet-1 POST
        
        #asociar otra interfaz a subnet-2 POST

        #configurar gateway POST

        #####FIN ACTIVIDAD 5#####
        break
    elif actividad=="6":
        #####INICIO ACTIVIDAD 6#####
        #SSH
        #####FIN ACTIVIDAD 6#####
        break
    else:
        print ("No haz seleccionado una opción disponible, finalizando programa.")
        break
   









