#! C:\Program Files (x86)\Python
# -*- coding: iso-8859-15 -*-
import os, sys

n = int(input("Ingrese la cantidad a comprar: "))
p = float(input("Ingrese el precio unitario: "))
if n >= 6:
    descuento_1 = 0.15 * p
    descuento_total = p-descuento_1
else:
    descuento_2 = 0.1 * p
    descuento_total = p-descuento_2
suma = n*descuento_total
print "El total a pagar es: $",suma