""" Si listamos todos los numeros naturales por debajo de 10 que son multiplos de 3 o 5,
obtenemos 3, 5, 6 y 9. La suma de estos multiplos es 23.
Encuentra la suma de todos los multiplos de 3 o 5 por debajo de 1000"""

suma = 0
for numero in range (0, 1000):
    if numero % 3 == 0 or numero % 5 == 0:
        suma = suma + numero
print(suma)
