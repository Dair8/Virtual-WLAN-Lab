Virtual-WLAN-Lab
================
Repositorio que contiene el Trabajo Fin de Grado relacionado con el diseño e implementación de un Laboratorio Virtual de Redes Inalámbricas.

###Requisitos
- Hosts: N Máquinas Virtuales con Linux
- Controller: 1 Máquina Virtual con Linux
- Hosts: En el caso de querer utilizar AODV, instalar AODV-UU: https://github.com/erimatnor/aodv-uu requiere kernel 2.6.x y módulo Netfiler.

###Instrucciones
- Hosts: Iniciar Máquinas Virtuales y ejecutar host.py: "sudo python host.py"
- Controller: Modificar data.json como se quiera y ejecutar controller.py: "sudo python controller.py -t IPHost1,IPHost2,...,IPHostN" Se proporciona un JSON para comprobar la estructura del mismo.
- Hosts: Lanzar AODV-UU: "sudo modprobe kaodv" "sudo aodvd -i tun0 -l -r 2"
