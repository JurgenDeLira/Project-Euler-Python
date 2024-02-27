"""Cada nuevo término en la secuencia Fibonacci es generado al añadir los dos terminos
anteriores. Al iniciar con 1 y 2, los primeros 10 términos seran:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89,....
Al considerar los términos en la secuencia Fibonacci cuyos valores no exceden los 4,000,000,
encuentra la suma de los términos con valores pares"""

num1 = 1
num2 = 2
num3 = num1 + num2

suma_numeros_pares = num2

lista_num_pares = [2]

while num3 < 4000000:
    num1 = num2
    num2 = num3
    num3 = num1 + num2
    
    if num3 % 2 == 0:
        suma_numeros_pares = suma_numeros_pares + num3
        lista_num_pares.append(num3)
        
print(suma_numeros_pares)

print(sum(lista_num_pares))