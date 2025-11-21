#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500 
precios_frutas["Pera"]= 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas["Banana"]=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

print(precios_frutas.keys())

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos={}

for i in range (5):
    nombre=input("Ingrese el nombre del contacto: ")
    if nombre in contactos:
        print("El contacto ya existe, ingrese un contacto nuevo: ")
        nombre=input("Ingrese el  número del contacto: ")
    num=int(input("Ingrese el número telefónico sin espacios: "))
    contactos[nombre]=num

pedir=input("Ingrese el nombre del contacto del cual desea encontrar el número telefónico: ")
  
if pedir in contactos:
    print(contactos[pedir])
else:
    print("El contacto no existe.")


#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase=input("Ingrese una frase: ")

palabras = frase.split()
#cantidad= len(palabras)
palabrasunicas=set(palabras)
print(f" {palabrasunicas}")

diccionario={}

for palabra in palabras:
    diccionario[palabra]= diccionario.get(palabra,0)+1

print(diccionario)   

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

def promedio(notas):
    suma = 0
    for n in notas:
        suma += n
    return suma / len(notas)


for i in range(3):
    alumno = input("Ingrese el nombre del alumno: ")
    lista_notas = []

    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {alumno}: "))
        lista_notas.append(nota)

    tupla_notas = tuple(lista_notas)
    prom = promedio(tupla_notas)

    print(f"Las notas de {alumno} son {tupla_notas} y su promedio es {prom}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

aprob1={"Ana", "Maria", "Carla", "Mateo", "Lola", "Juan"}
aprob2={"Ana", "Carla", "Mateo", "Lola"}

ambos= aprob1 & aprob2
solouno= aprob1 ^ aprob2
almenosuno= aprob1 | aprob1
print(f"Aprobaron ambos parciales {ambos}, aprobaron solo 1 parcial {solouno}, y aprobaron almenos 1 \nparcial {almenosuno}")


#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

diccionario = {"pan": 4, "agua": 8, "fideos": 5, "sal": 2, "harina": 4}

salir = False

while salir == False:
    consulta = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    consulta = consulta.lower().strip()

    if consulta == "salir":
        salir = True

    elif consulta in diccionario:
        print(f"Stock actual de {consulta}: {diccionario[consulta]} unidades")

        agregar = input("¿Desea agregar unidades a este producto? (si/no): ").lower().strip()
        if agregar == "si":
            cantidad = int(input("¿Cuántas unidades desea agregar?: "))
            diccionario[consulta] += cantidad
            print(f"Nuevo stock de {consulta}: {diccionario[consulta]} unidades")

    else:
        print("El producto ingresado no existe.")
        agregar = input("¿Desea agregarlo como nuevo producto? (si/no): ").lower().strip()
        if agregar == "si":
            cantidad = int(input("Ingrese el stock inicial: "))
            diccionario[consulta] = cantidad
            print(f"Producto {consulta} agregado con stock {cantidad} unidades.")


#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {("Lunes", "10:00"): "Ir al médico", ("Lunes", "15:30"): "Clase de programación",
("Martes", "09:00"): "Reunión de trabajo"}

print (agenda)

dia = input("Ingrese el día que desea consultar: ").capitalize().strip()
hora = input("Ingrese el horario que desea consultar (hh:mm): ").strip()

print(agenda.get((dia, hora), "No hay evento en ese horario."))


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores

paises_capitales = {
    "Argentina": "Buenos Aires",
    "España": "Madrid",
    "Francia": "París",
    "Japón": "Tokio",
    "México": "Ciudad de México"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(capitales_paises)