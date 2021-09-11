### README - ROYER YANGALI CÁCERES ###

¡Hola!, este es mi archivo de documentación muy resumido.

- El programa consta de 2 scripts python: "Main.py" y "obtener_token.py", los que se detallan a continuación.

        "obtener_token": el fin de este script es para obtener el token que nos servirá para realizar operaciones CRUD en las distintas APIS
        de los distintos servicios de Open Stack, operaciones como listar/crear/borrar/actualizar redes, subredes, instancias, flavors, entre otros.
        Inicialmente busqué la forma de automatizarlo; de modo que el copy-paste de este token hacia "Main.py" no fuera manual. Sin embargo, por temas
        de tiempo no lo pude realizar.

        "Main.py": es el programa principal, basado en un mini menú (que no está validado del todo, pueden encontrar bugs), se realizan las operaciones
        lo más parecido a las desarrolladas en la guía de laboratorio de OpenStack desarrollado por ustedes en el workshop. Como en python 3 no se cuenta 
        con el SWITCH-CASE, encontrán el menú en base a sentencias IF-ELIF. 

- Se tiene dos archivos secundarios: "clouds.yaml" y "LogsDeOpenStack.log", los que también son detallados a continuación:

        "clouds.yaml": básicamente es el archivo que contiene al configuración y parámetros necesarios para poder conectarnos a la API central de gestión 
        de OpenStack mediante el método de IP Interno (intenté buscar conexión mediante IP externa sin éxito :sadface:). A partir de esta conexión, que es la
        que se ejecuta primero en el script "Main.py", se logrará conectar internamente a distintos APIS de distintos servicios de OpenStack.

        "LogsDeOpenStack.log": nos muestra información de login generados por la conexión a la API central de OpenStack. Muy útil en temas de seguridad.

Finalmente, la mayoría del código está comentado y estructurado de la forma más ordenada posible; ¡espero que puedan disfrutarlo! (aún cuando no lo logré acabar).

Best Regards,
Royer Yangali Cáceres.




#######################################CREDENCIALES WHITESTACK#######################################
pod08:
horizon:
password: vC3kwt5Yhkd4rewtRFF365TbHT8TuYo1lFaTbH4x
url: http://139.178.85.7:1008
username: admin
internal_ip: 192.168.0.80
servers:
rancher:
Networks:
PRIVATE:
- 172.31.0.97
- 10.10.8.252
webterminal:
password: 95f7104c40281877f436c0efc4c8cffa
url: http://139.178.85.7:8080/remote
username: pod08
#######################################################################################################