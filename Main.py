#Librerías que se usarán
import argparse
import os
import sys
import openstack
from openstack import image
from openstack.config import loader
from openstack import connection

##########################################################INICIALIZACIÓN#########################################
# Para tener los logs en el archivo "LogsDeOpenStack"
openstack.enable_logging(True, path="LogsDeOpenstack.log", stream=sys.stdout)

# Se realiza la conexión a la API openstack mediante el uso del archivo clouds.yaml que ha sido descargado. Por defecto, se realizará la búsqueda en el mismo path del proyecto:
conn = openstack.connect(cloud="openstack")
##########################################################FIN INICIALIZACIÓN#########################################


# Listamos las instancias que están creadas:
for server in conn.compute.servers():
    print(server.to_dict())

