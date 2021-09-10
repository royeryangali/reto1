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

# Listamos los endpoints:
f.write("Lista de endpoints: \n")
for endpoints in conn.identity.endpoints():
    print(endpoints.name)    
f.write("\n")

# Listamos los proyectos:
f.write("Lista de proyectos: \n")
for project in conn.identity.projects():
    print(project.name)   
f.write("\n")

# Listamos los usuarios:
f.write("Lista de usuarios: \n")
for user in conn.identity.users():
    print(user.name)   
f.write("\n")

f.close()