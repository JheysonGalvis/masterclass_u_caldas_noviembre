# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 18:43:53 2025

@author: yeiso
"""

import math as m
import random

# Variables
Pi = m.pi  # Constante PI
print(Pi)

print(m.sin(m.radians(45)))  # Seno de 45°
print(m.cos(m.radians(0)))   # Coseno de 0°

print(m.ceil(5.00001))       # Redondea al entero máximo posible
print(m.floor(5.89462))      # Redondea al entero mínimo posible

print(m.e)                   # Constante de Euler

print(m.fabs(-789))          # Valor absoluto de un número
print(m.sqrt(49))            # Raíz cuadrada de un número
print(m.pow(9, 2))           # Potencia (9 elevado a 2)
print(m.factorial(7))        # Factorial de 7
print(m.hypot(4, 3))         # Hipotenusa (teorema de Pitágoras)

# Números aleatorios
var1 = random.randint(1, 20)  # Número entero aleatorio entre 1 y 20
print(var1)

var2 = random.random()        # Número aleatorio entre 0 y 1
print(var2)

# Redondear decimales
print(round(4.56878, 1))      # Redondea a 1 decimal
