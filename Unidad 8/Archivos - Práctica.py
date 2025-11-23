#Creo una función que recorra las lineas y los elementos para poder utilizarla en los momentos que 
#la precise
def lectura(contenidoxlinea):
    #recorro las lineas del archivo
    for linea in contenidoxlinea:
        #con strip limpio los espacios y con split separo las palabras de la linea
        #para poder trabajar sin errores  
        linealimpia = linea.strip()
        palabras = linealimpia.split(",")
        #por posición de elemento, asigno mediante un string su denominación esperada
        palabras[0] = f"Producto: {palabras[0]} |"
        palabras[1] = f" Precio: ${palabras[1]} |"
        palabras[2] = f" Cantidad: {palabras[2]}"
        #Creo el mensaje concatenando y lo muestro
        lista = f"{palabras[0]}{palabras[1]}{palabras[2]}"
        print(lista)   

#Abro y leo el archivo
with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
#recorro y separo las lineas del archivo
contenidoxlinea = contenido.splitlines()
#Llamo la función con el parámetro correspondiente
lectura(contenidoxlinea)

#Le pido al usuario que agregue un nuevo producto
agregar = input("Agregue un nuevo producto en el formato nombre,precio,cantidad: ").strip()
#Abro el archivo con el modo append para poder agregar el nuevo producto
with open("productos.txt", "a") as archivo:
    #concateno con un salto de linea para que se genere una nueva fila
    archivo.write("\n" + agregar)
#Abro el archivo en modo lectura para poder recorrer sus lineas contando la nueva carga
with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
contenidoxlinea = contenido.splitlines()
#Vuelvo a llamar la función con la nueva carga ya incluida en la lectura de lineas
lectura(contenidoxlinea)

#creo una lista
productos = []
#Printeo un salto de linea para una mejor interfaz 
print("\n")

#Recorro las lineas para delimitar que los elementos por linea sean 3, de ese modo el programa no tirará 
#error al intentar crear el diccionario.
for linea in contenidoxlinea:
    linealimpia = linea.strip()
    if not linealimpia:
        continue  
    #Separo los elementos de las lineas
    partes = linealimpia.split(",")
    #Me aseguro que sean 3 elementos para respetar el orden, si no lo son salto esa linea
    if len(partes) != 3:
        continue  

    nombre, precio, cantidad = partes
    #Creo el diccionario, utilizando como key un string descriptivo y como valor el elemento de la fila
    #correspondiente.
    producto_dict = {
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    #Por vuelta del for voy agregando los datos de cada fila y lo muestro
    productos.append(producto_dict)
    print(producto_dict)
print("\n")

#Doy la opción de buscar un producto al usuario
nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
#creo una variable de validación
encontrado = False
print("\n")

#recorro la lista de productos si coincide el nombre buscado con los existenes 
for p in productos:
    if p["nombre"].lower() == nombre_buscar.lower():
        #si existe, se imprime la fila a la que corresponde
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break 

if not encontrado:
    print("Error: el producto no existe en la lista.")
    

#guardo todos los cambios pisando el contenido anterior
with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

