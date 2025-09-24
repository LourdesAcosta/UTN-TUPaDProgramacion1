
#Lourdes Abril Acosta Muñoz
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad= int(input("Ingrese su edad:"))
edad_mayor= 18
if edad >edad_mayor:
    print("Es mayor de edad")
else:
    pass

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota= int(input("Ingrese su nota:"))
aprobado= 6

if nota >= aprobado :
    print("Aprobado")
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero=int(input("Ingrese un número par:"))

if numero % 2 == 0 :
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad= int(input("Ingrese su edad:"))

if edad < 12 and edad > 0 :
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a mayor")
else:
    print("Edad invalida")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contrasena= input("Ingrese una contraseña de 8 a 14 caracteres:")

if len(contrasena) >= 8 and len(contrasena)<= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6)escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
numeros_aleatorios = [random.randint(1,100) for i in range (50)]

from statistics import mode, median, mean
moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)


if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana< moda :
    print("Sesgo negativo o a la izquierda")
else:
    print("No hay sesgo")

print(numeros_aleatorios)
print("Moda: " ,moda)
print("Mediana: ", mediana)
print("Media: ", media) 

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

fraseopalabra= input("Ingrese una frase o palabra:")

if fraseopalabra != " ":
   ultima= fraseopalabra[-1].lower()
   if ultima in "aeiou":
      fraseopalabra += "!"
      print(fraseopalabra)
   else :
     print(fraseopalabra)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre:")
numero = int(input("Ingrese 1. Si quiere su nombre en mayúsculas. \n Ingrese 2. Si quiere su nombre en minúsculas. \n Ingrese 3. Si quiere su nombre con la primera letra mayúscula. "))

if numero == 1 :
   print(nombre.upper())
elif numero == 2 :
   print(nombre.lower())
elif numero == 3 :
   print(nombre.title())
else :
   print("Ha ingresado un número invalido.")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud = float(input("Ingrese la magnitud del terremoto:"))

if magnitud < 3 :
    print("Muy leve \n Imperceptible")
elif magnitud >= 3 and magnitud < 4 :
    print("Leve \n Ligeramente perceptible")
elif magnitud >= 4 and magnitud <5 :
    print("Moderado \n Sentido por personas, pero generalmente no causa daños")
elif magnitud >=5 and magnitud <6 :
    print("Fuerte \n Puede causar daños en estructuras débiles ")
elif magnitud >=6 and magnitud <7 :
    print("Muy fuerte \n Puede causar daños significativos")
elif magnitud >=7 :
    print("Exremo \n Puede causar graves daños a gran escala")
else:
    print("Ingrese un número válido.")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio= input("Ingrese en el hemisferio que se encuentra: \nN: Norte \nS: Sur \n")
mes = int(input("Ingrese el mes del año en el que se encuentra en formato numérico: "))
dia = int(input("Ingrese el día del año: "))
hemisferio=hemisferio.lower()

    #Invierno en el hemisferio norte:
if hemisferio=="n" and mes==12 and dia >= 21 and dia<= 31:
    print("Se encuentra en la estación Invierno.")
elif hemisferio=="n" and mes==1 and dia >= 1 and dia<= 31:
    print("Se encuentra en la estación Invierno.")
elif hemisferio=="n" and mes==2 and dia >= 1 and dia<=28 :
    print("Se encuentra en la estación Invierno.")
elif hemisferio=="n" and mes==3 and dia >= 1 and dia<=20 :
    print("Se encuentra en la estación Invierno.")
    #Verano en el hemisferio sur:
elif hemisferio=="s" and mes==12 and dia >= 21 and dia<= 31:
    print("Se encuentra en la estación Verano.")
elif hemisferio=="s" and mes==1 and dia >= 1 and dia<= 31:
    print("Se encuentra en la estación Verano.")
elif hemisferio=="s" and mes==2 and dia >= 1 and dia<=28 :
    print("Se encuentra en la estación Verano.")
elif hemisferio=="s" and mes==3 and dia >= 1 and dia<=20 :
    print("Se encuentra en la estación Verano.")
    #Primavera en el hermisferio norte:
elif hemisferio=="n" and mes==3 and dia >= 21 and dia<= 31:
    print("Se encuentra en la estación Primavera.")
elif hemisferio=="n" and mes==4 and dia>= 1 and dia<= 30 :
    print("Se encuentra en la estación Primavera.")
elif hemisferio=="n" and mes==5 and dia>= 1 and dia<= 31 :
    print("Se encuentra en la estación Primavera.")
elif hemisferio=="n" and mes==6 and dia>= 1 and dia<= 20:
    print("Se encuentra en la estación Primavera.")
    #Otoño en el hemisferio sur:
elif hemisferio=="s" and mes==3 and dia >= 21 and dia<= 31:
    print("Se encuentra en la estación Otoño.")
elif hemisferio=="s" and mes==4 and dia>= 1 and dia<= 30 :
    print("Se encuentra en la estación Otoño.")
elif hemisferio=="s" and mes==5 and dia>= 1 and dia<= 31 :
    print("Se encuentra en la estación Otoño.")
elif hemisferio=="s" and mes==6 and dia>= 1 and dia<= 20:
    print("Se encuentra en la estación Otoño.")
    #Verano en el hemisferio norte:
elif hemisferio=="n" and mes==6 and dia>= 21 and dia<= 30:
    print("Se encuentra en la estación Verano.")
elif hemisferio=="n" and (mes==7 or mes==8) and dia>= 1 and dia <=31:
    print("Se encuentra en la estación Verano.")
elif hemisferio=="n" and mes==9 and dia>=1 and dia<=30:
    print("Se encuentra en la estación Verano.")
    #Invierno en el hemisferio sur:
elif hemisferio=="s" and mes==6 and dia>= 21 and dia<= 30:
    print("Se encuentra en la estación Invierno.")
elif hemisferio=="s" and (mes==7 or mes==8) and dia>= 1 and dia <=31:
    print("Se encuentra en la estación Invierno.")
elif hemisferio=="s" and mes==9 and dia>=1 and dia<=20:
    print("Se encuentra en la estación Invierno.")
    #Otoño en el hemisferio norte:
elif hemisferio=="n" and mes==9 and dia>=21 and dia<=30:
    print("Se encuentra en la estación Otoño.")
elif hemisferio=="n" and mes==10 and dia>=1 and dia<=31:
    print("Se encuentra en la estación Otoño.")
elif hemisferio=="n" and mes==11 and dia>=1 and dia<=30:
    print("Se encuentra en la estación Otoño.")
elif hemisferio=="n" and mes==12 and dia>=1 and dia<=20:
    print("Se encuentra en la estación Otoño.")
    #Primavera en el hemisferio sur:
elif hemisferio=="s" and mes==9 and dia>=21 and dia<=30:
    print("Se encuentra en la estación Primavera.")
elif hemisferio=="s" and mes==10 and dia>=1 and dia<=31:
    print("Se encuentra en la estación Pimavera.")
elif hemisferio=="s" and mes==11 and dia>=1 and dia<=30:
    print("Se encuentra en la estación Primavera.")
elif hemisferio=="s" and mes==12 and dia>=1 and dia<=20:
    print("Se encuentra en la estación Primavera.")
else:
    print("Fecha o hemisferio ingresado invalido.")







