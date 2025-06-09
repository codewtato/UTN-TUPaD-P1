#Importe time para medir cuanto tiempo tarda cada algoritmo
import time

# ORDENAMIENTO POR BURBUJA
#Definimos el ordenamiento por burbuja que recibe lista como parametro
def bubble_sort(lista):
    #Obtenemos el tamaño de la lista
    n = len(lista)
    #Pasamos al primer bucle que controla la cantidad de pasadas
    for i in range(n):
        #Este bucle compara los elementos adyacentes desde el principio hasta la parte que ya esta ordenada
        for j in range(0, n - i - 1):
            #Formula del ordenamiento por burbuja, si el elemento es mayor al siguiente los intercambia
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                #Devuelvo lista
    return lista

# BÚSQUEDA POR INTERPOLACIÓN
#Defino busqueda por interpolacion y pasamos lista y objetivo como parametros
def busqueda_interpolacion(lista, objetivo):
    #Inicializo izquierda y derecha
    izquierda = 0
    derecha = len(lista) - 1
    #Verificamos si hay elementos para revisar y que el numero este dentro del rango
    while izquierda <= derecha and lista[izquierda] <= objetivo <= lista[derecha]:
        #Revisamos si queda solo un numero y comparamos si es el que buscamos
        if izquierda == derecha:
            if lista[izquierda] == objetivo:
                return izquierda
            #Devuelve -1 si no esta
            return -1
        #Formula de busqueda por interpolacion, calcula masomenos donde puede estar.
        pos = izquierda + ((objetivo - lista[izquierda]) * (derecha - izquierda) //
                          (lista[derecha] - lista[izquierda]))
        #Si justo en esa posición calculada esta el numero que pedimos como objetivo, significa que lo encontramos y nos devuelve el numero.
        if lista[pos] == objetivo:
            return pos
        #Verificamos si el numero que en pos es menor al objetivo
        elif lista[pos] < objetivo:
            izquierda = pos + 1
        #Verificamos si el numero que en pos es mayor al objetivo
        else:
            derecha = pos - 1
            #Devuelvo -1 si todo eso no pasa
    return -1


# PRUEBAS


lista = list(range(1, 10001))     
objetivo = 10000               

# ORDENAMIENTO
print("=== ORDENAMIENTO (Bubble Sort) ===")
#Desordeno la lista para que trabaje el ordenamiento
lista_desordenada = lista[::-1]
#Marcamos el inicio
inicio = time.perf_counter()
#Aplicamos el ordenamiento por burbuja sobre una copia de la lista
ordenada = bubble_sort(lista_desordenada.copy())
#Marcamos el final
fin = time.perf_counter()
#Mostramos por pantalla la lista ordenada
print("Lista ordenada:", ordenada)
#Muestro cuanto tardo, con 10 decimales para ver bien
print(f"Tiempo de ordenamiento: {fin - inicio:.10f} segundos\n")

# BÚSQUEDA
print("=== BÚSQUEDA (Interpolación) ===")
#Marcamos el inicio
inicio = time.perf_counter()
#Buscamos el numero en la lista ya ordenada y le pasamos un objetivo como parametro
posicion = busqueda_interpolacion(ordenada, objetivo)
#Marcamos el final
fin = time.perf_counter()
#Mostramos que numero se esta buscando
print(f"Elemento buscado: {objetivo}")
#Mostramos si se encontro
print(f"Encontrado en posición: {posicion}" if posicion != -1 else "No encontrado.")
#Mostramos cuanto tardo en hacer la busqueda
print(f"Tiempo de búsqueda: {fin - inicio:.10f} segundos")
