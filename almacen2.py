#! C:\Program Files (x86)\Python
# -*- coding: iso-8859-15 -*-
import os, sys

n = int(input("Ingrese la cantidad a comprar: "))
p = 10000

if n >= 10:
    descuento_1 = 0.25 * p
    descuento_total = p-descuento_1
elif (n >= 5) and (n <= 9):
    descuento_2 = 0.2 * p
    descuento_total = p-descuento_2
elif (n >= 0) and (n <= 4):
    descuento_3 = 0.15 * p
    descuento_total = p-descuento_3

suma = n*descuento_total
print "El total a pagar es: $",suma