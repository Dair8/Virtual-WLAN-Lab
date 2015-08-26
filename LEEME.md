Virtual-WANET-Lab
================
Repositorio que contiene el Trabajo Fin de Grado relacionado con el diseño e implementación de un Laboratorio Virtual de Redes Ad-hoc Inalámbricas.

###Requisitos
- Hosts: N Máquinas Virtuales con Ubuntu 10.04 u otra Distribución de Linux con kernel 2.6.x, y el módulo Netfiler instalado
- Controller: 1 Máquina Virtual con Linux
- Hosts: Instalar AODV-UU: https://github.com/erimatnor/aodv-uu

###Instrucciones
- Hosts: Iniciar Máquinas Virtuales y ejecutar host.py: "sudo python host.py"
- Controller: Modificar data.json como se quiera y ejecutar controller.py: "sudo python controller.py -t IPHost1,IPHost2,...,IPHostN" Se proporciona un JSON para comprobar la estructura del mismo.
- Hosts: Lanzar AODV-UU: "sudo modprobe kaodv" "sudo aodvd -i tun0 -l -r 2"
