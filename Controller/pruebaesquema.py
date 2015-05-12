# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import json
from NetScheme import NetScheme

with open('data.json') as data_file:    
    data = json.load(data_file)
print("Creacion e impresion del esquema a partir del json")
esquema=NetScheme(data["hosts"],data["neighbors"])
esquema.printScheme()

print("\nAdicion de un nuevo Host e impresion de la nueva lista")
esquema.addHost("E")
esquema.printHosts()

print("\nAdicion de vecinos al nuevo host e impresion de sus vecinos")
esquema.setNeighbors("E","A")
print(esquema.getNeighbors("E"))

print("\nImpresion del nuevo esquema")
esquema.printScheme()

print("\nSupresion de vecinos del host E e impresion de sus vecinos")
esquema.delNeighbors("E")
print(esquema.getNeighbors("E"))

print("\nEliminacion del Host E e impresion del esquema de red")
esquema.delHost("E")
esquema.printScheme()