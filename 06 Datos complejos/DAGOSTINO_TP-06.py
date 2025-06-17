
# TP 6 - Estructuras de datos complejas - SIN OBJETOS

# 1) Dado el diccionario precios_frutas
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios.
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# 4) Agenda telefónica

agenda = {}

def agregar_contacto():
    if len(agenda) >= 5:
        print("Ya cargaste los 5 contactos permitidos.")
        return
    
    nombre = input("Ingresá el nombre del contacto: ")
    if nombre in agenda:
        print("Ese contacto ya fue ingresado.")
        return
    
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero
    print(f"Contacto '{nombre}' agregado correctamente.")

def buscar_contacto():
    nombre = input("Ingresá el nombre del contacto que querés buscar: ")
    if nombre in agenda:
        print(f"Número de {nombre}: {agenda[nombre]}")
    else:
        print("Ese contacto no está en la agenda.")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intentá de nuevo.")
conteo = {}
# 5) Análisis de frase
frase = input("Ingresá una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("Cantidad de apariciones:", conteo)


# 6) Promedio de notas de 3 alumnos
alumnos = {}

for _ in range(3):
    nombre = input("Ingresá el nombre del alumno: ")
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Ingresá la nota {i} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\n--- Promedios ---")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

# 7) Análisis de sets de estudiantes
parcial1 = {"Ana", "Juan", "Pedro", "Lucía"}
parcial2 = {"Lucía", "Juan", "Sofía", "Carlos"}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("\n--- Aprobados en ambos parciales ---")
print(ambos)

print("\n--- Aprobados solo en uno de los dos parciales ---")
print(solo_uno)

print("\n--- Total de estudiantes que aprobaron al menos un parcial ---")
print(al_menos_uno)

# 8) Stock de productos
stock = {}

def consultar_stock():
    producto = input("Ingresá el nombre del producto: ")
    if producto in stock:
        print(f"Stock de {producto}: {stock[producto]} unidades.")
    else:
        print(f"El producto '{producto}' no está registrado.")

def agregar_stock():
    producto = input("Ingresá el nombre del producto: ")
    if producto in stock:
        cantidad = int(input(f"¿Cuántas unidades querés agregar a '{producto}'? "))
        stock[producto] += cantidad
        print(f"Stock actualizado: {stock[producto]} unidades.")
    else:
        print(f"El producto '{producto}' no existe. Usá la opción 3 para agregarlo.")

def agregar_nuevo_producto():
    producto = input("Ingresá el nombre del nuevo producto: ")
    if producto in stock:
        print("Ese producto ya existe. Usá la opción 2 para agregar stock.")
    else:
        cantidad = int(input(f"Ingresá la cantidad inicial para '{producto}': "))
        stock[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")

# Menú principal
while True:
    print("\n--- MENÚ DE STOCK ---")
    print("1. Consultar stock")
    print("2. Agregar stock a producto existente")
    print("3. Agregar nuevo producto")
    print("4. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        consultar_stock()
    elif opcion == "2":
        agregar_stock()
    elif opcion == "3":
        agregar_nuevo_producto()
    elif opcion == "4":
        print("Saliendo del sistema de stock...")
        break
    else:
        print("Opción inválida. Intentá de nuevo.")

# 9) Agenda con tuplas
agenda = {}

def agregar_evento():
    dia = input("Ingresá el día (ej: lunes): ").capitalize()
    hora = input("Ingresá la hora (ej: 14:00): ")
    clave = (dia, hora)
    if clave in agenda:
        print(f"Ya hay un evento programado: {agenda[clave]}")
    else:
        evento = input("Ingresá el nombre del evento: ")
        agenda[clave] = evento
        print("Evento agregado correctamente.")

def consultar_evento():
    dia = input("Ingresá el día del evento: ").capitalize()
    hora = input("Ingresá la hora del evento: ")
    clave = (dia, hora)
    if clave in agenda:
        print(f"Evento en {dia} a las {hora}: {agenda[clave]}")
    else:
        print("No hay ningún evento agendado en ese horario.")

def mostrar_todos():
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("\n--- Todos los eventos agendados ---")
        for (dia, hora), evento in sorted(agenda.items()):
            print(f"{dia} a las {hora} → {evento}")

# Menú principal
while True:
    print("\n--- AGENDA ---")
    print("1. Agregar evento")
    print("2. Consultar evento")
    print("3. Mostrar todos los eventos")
    print("4. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        agregar_evento()
    elif opcion == "2":
        consultar_evento()
    elif opcion == "3":
        mostrar_todos()
    elif opcion == "4":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción inválida. Intentá de nuevo.")

# 10) Invertir diccionario país-capital
paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Italia": "Roma",
    "España": "Madrid",
    "Brasil": "Brasilia"
}

capitales_a_paises = {}

for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

print("\n--- Diccionario invertido (capitales → países) ---")
for capital, pais in capitales_a_paises.items():
    print(f"{capital} → {pais}")