#Trabajo Práctico N°4, Estructuras Repetitivas
#Lourdes Abril Acosta Muñoz

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea

for i in range(0,101):
    print( i )


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num=int(input("Ingrese un número entero: "))
num_entero=abs(num)
contador_digitos=0

while num_entero > 0:
    contador_digitos += 1
    num_entero= num_entero//10

print(f"El número {num} contiene {contador_digitos} digitos.")   



#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores. 
            
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
inicio= num1
fin=num2
resultado=0

if num1>num2:
     num1,num2=num2,num1

for i in range(num1+1, num2):
      resultado += i
      
print(f"La suma de todos los número comprendidos entre {inicio} y {fin} es {resultado}")



#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num=int(input("Ingrese un número entero: "))
contador=0
while num !=0 :
    contador+=num
    num=int(input("Ingrese otro número entero: "))

print(f"La suma de todos los número ingresados es de {contador}.")



#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_random= random.randint(0,9)
i=1

num=int(input("Ingrese un núermo del 0 al 9: "))
while num != numero_random:
    num=int(input("Incorrecto, ingrese otro núermo del 0 al 9: "))
    i +=1

print(f"Usted requirió de {i} intentos para adivinar el número {numero_random} ")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100,-1,-2):
    print(i)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
resultado=0
num=int(input("Ingrese un número entero positivo: "))

while num < 0 :
    print("El número ingresado no cumple con los parámetros.")
    num=int(input("Ingrese un número entero positivo: "))

for i in range(0,num+1):
    resultado += i

print(f"La suma de todos los números enteros comprendidos entre 0 y {num} es {resultado}")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
num_negativo=0
num_positivo=0
num_par=0
num_impar=0

for i in range(100):
    num=int(input("Ingrese un número: ")) 
    if num > 0 and num %2 ==0 :
        num_positivo+=1
        num_par +=1
    elif num > 0 and num %2 !=0 :
         num_positivo+=1
         num_impar +=1
    if num < 0 and num % 2 == 0:
        num_negativo +=1
        num_par +=1
    elif num < 0 and num % 2 != 0:
        num_negativo +=1
        num_impar +=1
       
print(f"La cantidad de número pares es de {num_par}, de números impares es {num_impar},\n de números positivos es {num_positivo}, y de números negativos es {num_negativo}")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
suma=0
rango=10
for i in range(rango):
    num=int(input("Ingrese un número: "))
    suma+=num

media=suma/rango

print(f"La media de los valores ingreados es de {media} ")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num_original=int(input("Ingrese un número: "))
num=num_original
conversion=0
while num >0:
    digitos=num%10 
    conversion= conversion * 10 + digitos
    num=num//10

print(f"Su número original es {num_original} y el invertido es {conversion}")