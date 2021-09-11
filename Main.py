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
            print(server.name)
            f.write("Name: "+ server.name + " | ")
            f.write("Hostname: " + server.hostname + " | ")            
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
        f.close()
        break

    elif actividad=="2":
        g = open("2OutputAct.txt","w")
        #####INICIO ACTIVIDAD 2#####
        os.system('source /etc/whitecloud/admin-openrc.sh')
        os.system('openstack server list')        
        #####FIN ACTIVIDAD 2#####
        g.write("Credenciales de admin cargadas.\n")
        g.close()
        break
    elif actividad=="3":
        #####INICIO ACTIVIDAD 3#####
        #####FIN ACTIVIDAD 3#####
        break
    elif actividad=="4":
        #####INICIO ACTIVIDAD 4#####
        #####FIN ACTIVIDAD 4#####
        break
    elif actividad=="5":
        #####INICIO ACTIVIDAD 5#####
        #####FIN ACTIVIDAD 5#####
        break
    elif actividad=="6":
        #####INICIO ACTIVIDAD 6#####
        #####FIN ACTIVIDAD 6#####
        break
    else:
        print ("No haz seleccionado una opción disponible, finalizando programa.")
        break
   









