Virtual-WLAN-Lab
================
Repository that hosts the Final Project related to the design and implementation of a Virtual Laboratory of Wireless Networks.

###Requirements
- Hosts: N Virtual Machines with Linux.
- Controller: 1 Virtual Machine with Linux
- Hosts: In case of wanting to use AODV, install AODV-UU: https://github.com/erimatnor/aodv-uu it requires kernel 2.6.x, and the Netfiler module.

###Instructions
- Hosts: Initiate the Virtual Machines and launch host.py: "sudo python host.py"
- Controller: Modify data.json as wished and launch controller.py: "sudo python controller.py -t IPHost1,IPHost2,...,IPHostN" A JSON is already provided in order to check the structure.
- Hosts: Launch AODV-UU: "sudo modprobe kaodv" "sudo aodvd -i tun0 -l -r 2"
