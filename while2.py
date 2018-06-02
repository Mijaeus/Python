#! C:\Program Files (x86)\Python
# -*- coding: iso-8859-15 -*-
import os, sys

from random import *
x = 0
i = 0
while True:
    x = randint(1, 1000)
    print "Resultado lanzamiento:", x
    i += 1
    if x == 5:
        break
    print "Numero de intentos:", i