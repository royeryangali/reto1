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

##Crear un txt para guardar las salidas que nos interesan:
f = open("OutputRoyer.txt","w")
###
# Listamos las instancias que están creadas:
for server in conn.compute.servers():
    print(server.name)
    f.write(server.name)

f.write("\n","w")
# Listamos las imágenes disponibles:
for image in conn.compute.images():
    print(image.name)
    f.write(image.name)

f.close()