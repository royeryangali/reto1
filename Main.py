import argparse
import os
import sys
import subprocess
import openstack
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
f = open("OutputRoyer.txt","w")
###

print("ACTIVIDADES LABORATORIO WHITESTACK")
print("1.\n")
print("2.\n")
print("3.\n")
print("4.\n")
print("5.\n")
print("6.\n")

actividad = int(input("Seleccione el número de actividad a elegir: "))

#####INICIO ACTIVIDAD 1#####
# Listamos las instancias que están creadas:
f.write("Lista de instancias creadas:\n")
for server in conn.compute.servers():
    print(server.name)
    f.write(server.name + " | ")

f.write("\n")

# Listamos las imágenes disponibles:
f.write("Lista de imágenes disponibles:\n")
for image in conn.compute.images():
    print(image.name)
    f.write(image.name + " | ")
f.write("\n")

# Listamos los flavors disponibles:
f.write("Lista de flavors disponibles:\n")
for flavor in conn.compute.flavors():
    print(flavor.name)
    f.write(flavor.name + " | ")
f.write("\n")
#####FIN ACTIVIDAD 1#####

#####INICIO ACTIVIDAD 2#####
subprocess.call('sudo source /etc/whitecloud/admin-openrc.sh')
#####FIN ACTIVIDAD 2#####
f.write("Credenciales de admin cargadas.\n")

#####INICIO ACTIVIDAD 3#####
#####FIN ACTIVIDAD 3#####

#####INICIO ACTIVIDAD 4#####
#####FIN ACTIVIDAD 4#####

#####INICIO ACTIVIDAD 5#####
#####FIN ACTIVIDAD 5#####

#####INICIO ACTIVIDAD 6#####
#####FIN ACTIVIDAD 6#####

f.close()