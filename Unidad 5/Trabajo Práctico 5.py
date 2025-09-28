#Trabajo Práctico N°5
#Lourdes Abril Acosta Muñoz

#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

notas=[9,3,6,2,5,8,7,10,7,5]
cant_notas=len(notas)
sumatotal=0
print(f"La lista comppleta es: {notas}")

for i in range(cant_notas):
      suma=notas[i]
      sumatotal= sumatotal+suma

print(f"El promedio de todas las notas es de: {sumatotal/cant_notas}")

#ordernar lista

for pasada in range(cant_notas-1):
    intermabio=False
    for actual in range(cant_notas-1-pasada):
        if notas[actual] > notas[actual+1]:
          notas[actual], notas[actual+1] = notas[actual+1], notas[actual]
          intermabio = True
    if intermabio== False:
     print("La lista ya estaba ordenada.")
    break

print(f"La nota mas baja es {notas[0]} y la más alta es {notas[-1]}")


#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#3• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

lista=[]
seguir="si"

for i in range(5):
    productos = input(f"Ingrese el producto número {i+1} de la lista: ")
    lista.append(productos)

orden= sorted(lista)
print(orden)

while seguir=="si":
    eliminar=input(f"Desea eliminar algún producto de {orden}? \n Si/No: ")
    if eliminar.lower() == "si" or eliminar.lower()=="sí":
     producto_eliminado= input("Ingrese el nómbre del producto a eliminar: ")
     orden.remove(producto_eliminado)
     print(f"Lista actualizada: {orden}")
    actualizar= input(f"Desea actualizar algún producto de {orden}? \n Si/No: ")
    if actualizar.lower() == "si" or actualizar.lower()=="sí":
     elemento=input("Ingrese el nombre del elemento que desea actualizar: ")
     posicion=orden.index(elemento)
     orden[posicion] = input(f"Ingrese la actualización de {elemento}: ")
     print(f"Lista actualizada: {orden}")
    if seguir=="si":
       seguir=input("Desea continuar editando? \n Si/No:")
       seguir=seguir.lower()   
       seguir=seguir.strip()  

orden= sorted(orden)
print(f"Su lista actualizada es: {orden} ")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
numeros=[]
pares=[]
impares=[]
import random

for i in range(15):
    numeros.append(random.randint(1,100))

print(numeros)

for i in numeros:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Los números en la lista de pares son {pares} y la lista tiene {len(pares)} números.")
print(f"Los números en la lista de impares son {impares} y la lista tiene {len(impares)} números.")



#4)Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.
lista=[1,3,5,3,7,1,9,5,3]
orden=sorted(lista)
print(orden)
nueva_lista=[]

for num in orden:
    if num not in nueva_lista:
        nueva_lista.append(num)
         
print(nueva_lista)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

estudiantes=["juan","maria","pablo","clara","lara","marcos","sofia","mateo"]
continuar="si"
print(f"La lista de los nombres de estudiantes presentes es: {estudiantes}")

while continuar.lower().strip() == "si":
    #agregar el estudiante
    agregar=input("Desea agregar algún estudiante? \n Si/No: ")
    if agregar.lower().strip()=="si":
     nuevo_estudiante=input("Ingrese el nombre del estudinte que desea agregar: ")
     estudiantes.append(nuevo_estudiante)
     print(estudiantes)
    #eliminar estudiantes
    eliminar=input("Desea eliminar algún estudiante? \n Si/No: ")
    if eliminar.lower().strip()=="si":
     estudiante_eliminado=input("Ingrese el nombre del estudinte que desea eliminar: ")
     estudiantes.remove(estudiante_eliminado)
     print(estudiantes)
    continuar=input("Desea continuar editando? \n Si/No: ")

print(f"La lista final actualizada es: {estudiantes}")


#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

import random
lista=[]
cant_num=len(lista)

for i in range (7):
     lista.append(random.randint(1,100))
print(lista)

orden=sorted(lista)

print(orden)

orden = orden[-1:] + orden[:-1]

print("Lista rotada:", orden)


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

grados=[[13,19],[10,21],[13,22],[13,23],[11,21],[13,22],[16,24]]
sumamin=0
sumamax=0

#Mínima 
for i in range(len(grados)):
    sumamin+= grados[i][0]

print(f"El promedio de las mínimas es de {sumamin / len(grados)}")

#Máxima
for j in range(len(grados)):
    sumamax+= grados[j][1]

print(f"El promedio de las máximas es {sumamax/len(grados)}")

#Mayor amplitúd termica
maximaamplitud= float("-inf")

for dia in range(len(grados)):
    minima=grados[dia][0]
    maxima=grados[dia][1]
    maximatemperatura=maxima-minima
    if  maximaamplitud < maximatemperatura:
       maximaamplitud=maximatemperatura
       diadelamaxima=dia+1

print(f"El día que se registró la mayor aplitúd térmica fue el día {diadelamaxima} y la amplitúd fue de {maximaamplitud} grados aparte")



#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia

notas=[7,6,7],[8,4,5],[9,8,8],[3,6,7],[6,8,7]
sumanotas=0
estudiante=0
sumamateria1=0

#promedios por estudiante 
for i in notas:
   estudiante +=1
   for n in i:
    sumanotas += n
    promedio=sumanotas/len(i)
   print(f"El estudiante N° {estudiante} tiene un promedio de: {promedio}")
     
 #promedios por materia
notamateria=len(notas[0])
materia=len(notas)
for j in range(notamateria):
  sumamateria1=0
  for i in range (materia):
      sumamateria1+= notas[i][j]
      promediomateria=sumamateria1/materia
  print(f"El promedio de notas por materia es de: {promediomateria}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

tablero=[["-","-","-"]
        ,["-","-","-"],
         ["-","-","-"]]
filas=len(tablero)
columnas=len(tablero[0])
jugador1="X"
jugador2="O"
turno=jugador1

print("Jugador 1 eres: X \nJugador 2 eres: O")
print()

for i in range(filas-0):
    for j in range(columnas):
        print(tablero[i][j],end="  ")
    print()
print()


vuelta=0
#hasta hacer 9
while vuelta < filas*columnas:
    #posicion valida
    valido=False
    while not valido:
        print(f"Turno de: {turno}")
        numfila=int(input("Ingrese un número de fila (0,1,2): "))
        numcolumna=int(input("Ingrese un número de columna (0,1,2): "))

        if (numfila<0 or numfila>=filas) or (numcolumna<0 or numcolumna>=columnas):
            print("Fuera de rango")
        elif tablero[numfila][numcolumna] != "-":
            print("Posicion previamente seleccionada.")
        else:
            valido=True
     #poner la ficha
    
    tablero[numfila][numcolumna]=turno
    vuelta+=1
#mostrar tablero con jugada
    for i in range(filas):
        for j in range(columnas):
            print(tablero[i][j],end=" ")
        print()
    print()

    if turno==jugador1:
        turno=jugador2
    else:
        turno=jugador1
print("Tablero completo")


#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

registro=[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]

producto=[]
filas=len(registro)
columnas=len(registro[0])


for i in range(filas):
    nombreproducto=input("Ingrese en nombre del producto: ")
    producto.append(nombreproducto)
    for j in range(columnas):
        venta=int(input(f"Ingrese las ventas del producto {nombreproducto} el día {j+1}: "))
        registro[i][j] = venta

print()
#• Mostrar el total vendido por cada producto.
totalproducto=[0,0,0,0]
for i in range(filas):
    suma=0
    for j in range(columnas):
        suma = suma + registro[i][j]
    totalproducto[i] = suma
    print(f"{producto[i]}: {suma} unidades")

print()
#• Mostrar el día con mayores ventas totales.
max_dia_total = -1
dia_mayor = -1
for j in range(columnas):
    suma_dia = 0
    for i in range(filas):
        suma_dia = suma_dia + registro[i][j]
    if suma_dia > max_dia_total:
        max_dia_total = suma_dia
        dia_mayor = j + 1
print(f"El día con mayores ventas fue el día {dia_mayor} con {max_dia_total} unidades vendidas.") 


print()
#• Indicar cuál fue el producto más vendido en la semana.
max_prod_total = -1
indice_prod = -1
for i in range(filas):
    if totalproducto[i] > max_prod_total:
        max_prod_total = totalproducto[i]
        indice_prod = i
print(f"El producto más vendido fue: {producto[indice_prod]} con {max_prod_total} unidades vendidas.")

     