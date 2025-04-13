# Actividades
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un numero: "))
cantidad_digitos = len(str(numero))
print(f"El numero {numero} tiene {cantidad_digitos} digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
suma = 0
for i in range(n1 + 1, n2):
    suma += i
print(f"La suma de los numeros entre {n1} y {n2} es {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
while True:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break
    suma += numero
print(f"La suma de los numeros ingresados es {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intentos += 1
    numero_ingresado = int(input("Ingrese un numero: "))
    if numero_ingresado == numero_aleatorio:
        break
print(f"Lo lograste en {intentos} intentos")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un numero: "))
suma = 0
for i in range(numero + 1):
    suma += i
print(f"La suma de los numeros entre 0 y {numero} es {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(100):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Hay {pares} numeros pares, {impares} numeros impares, {positivos} numeros positivos y {negativos} numeros negativos")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma = 0
for i in range(100):
    numero = int(input("Ingrese un numero: "))
    suma += numero
media = suma / 100
print(f"La media de los numeros ingresados es {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un numero: "))
invertido = 0
while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10
print(f"El numero invertido es {invertido}")