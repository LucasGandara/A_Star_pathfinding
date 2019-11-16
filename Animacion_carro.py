#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author: Lucas G.
from os import system
import time
system('cls')
# Leemos los archivos
giros = open('tetas.txt', 'r')
ang = giros.read()
giros.close()

x = open('X.txt', 'r')
X = x.read()
x.close()

y = open('Y.txt', 'r')
Y = y.read()
y.close()

# Los formateamos
ang = ang.split()
Y = Y.split()
X = X.split()
angulo = [float(i) for i in ang]
ypos = [float(i) for i in Y]
xpos = [float(i) for i in X]


from turtle import *
color('red', 'yellow')
# Dibujamos segun los angulos
for i in range(14):
    left(angulo[i])
    goto(xpos[i] * 100, ypos[i] * 100)
    time.sleep(0.1)
done()