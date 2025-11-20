#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

name=input("Ingrese su nombre: ")
saludo=saludar_usuario(name)
print(saludo)


#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
   print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=int(input("Ingrese su edad: "))
residencia=input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
#y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
# y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para 
# mostrar los resultados.
import math

def  calcular_area_circulo(radio):
    area= math.pi * radio **2
    return area

def calcular_perimetro_circulo(radio):
    perimetro= 2 * math.pi * radio
    return perimetro

radio=int(input("Para calculr el area y perímetro de un círuclo ingrese el radio: "))
print(f"El area es de {calcular_area_circulo(radio)}, y el perímetro es de {calcular_perimetro_circulo(radio)}.")


#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas= segundos / 3600
    return horas

segundos=int(input("Ingrese una cantidad de segundos: "))
print(f"El equivalente de horas de {segundos} segundos es {segundos_a_horas(segundos)} horas")


#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i}= {numero * i}")

numero=int(input("Ingrese un número: "))
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
#y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    operaciones=(a+b, a-b, a*b, a/b )
    return operaciones

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el sgundo número: "))

resultados= operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura
#en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
# función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
     return round(peso / altura ** 2)


peso=float(input("Ingrese su peso en Kg: "))
altura=float(input("Ingrese sus altura en metros (x.xx): "))

print(F"Su Indice de masa corporal es de {calcular_imc(peso,altura)}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados 
#Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y 
# mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    conversion= (9/5) * celsius + 32
    return conversion

celcius=float(input("Ingrese una temperatura en formarto celcius: "))
print(f"{celcius}° celsius equivale a {celsius_a_fahrenheit(celcius)}° fahrenheit")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
#devuelva el promedio de ellos .
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    suma= (a + b + c )/ 3
    return suma

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
num3=int(input("Ingrese el tercer número: "))

print(f"El promedio entre los 3 múmeros es {calcular_promedio(num1,num2,num3)}")
  