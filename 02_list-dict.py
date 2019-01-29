#Ejercicio sobre listas
elementos = 0

#Crear una lista que contenga varios strings.
lista_de_strings = ["cadena 1" , "cadena 2" , "cadena 3" , "cadena 4" , "cadena 5"]

#Crear una lista que contenga varios integers
lista_de_enteros = [2, 4 , 6 , 8 , 10]

#Crear una lista que contenga strings, integers y floats
lista_variada = [1, "1", "entero", 3.15, "veintiseis"]

#Crear las sentencias necesarias para imprimir, por pantalla, la información de las listas.
print("La primera lista contiene: " , len(lista_de_strings) , " objetos; que son: " , lista_de_strings[0] ,
      type(lista_de_strings[0]), ", ", lista_de_strings[1] , type(lista_de_strings[1]) , ", ",  lista_de_strings[2] ,
      type(lista_de_strings[2]) , ", ",  lista_de_strings[3] , type(lista_de_strings[3]) , ", ",  lista_de_strings[4] ,
      type(lista_de_strings[4]), end = ". \n")
print("La segunda lista contiene: " , len(lista_de_enteros) , " objetos; que son: " , lista_de_enteros[0] ,
      type(lista_de_enteros[0]), ", ", lista_de_enteros[1] , type(lista_de_enteros[1]) , ", ",  lista_de_enteros[2] ,
      type(lista_de_enteros[2]) , ", ",  lista_de_enteros[3] , type(lista_de_enteros[3]) , ", ",  lista_de_enteros[4] ,
      type(lista_de_enteros[4]), end = ". \n")
print("La tercera lista contiene: " , len(lista_variada) , " objetos; que son: " , lista_variada[0] ,
      type(lista_variada[0]), ", ", lista_variada[1] , type(lista_variada[1]) , ", ",  lista_variada[2] ,
      type(lista_variada[2]) , ", ",  lista_variada[3] , type(lista_variada[3]) , ", ",  lista_variada[4] ,
      type(lista_variada[4]), end = ". \n")

#Crear 3 sentencias para asignar, en cada una, el último valor de una lista diferente a una variable (es decir, habrá 3
# variables, cada una con el último valor de una de las listas).
variable1 = lista_de_strings[4]
variable2 = lista_de_enteros[4]
variable3 = lista_variada[4]

#Crear una sentencia para imprimir, por pantalla, un texto, y concatenar la información de las variables.
print("Los últimos objetos de las listas son, respectivamente: ", variable1, ", ", variable2, " y ", variable3)

#Crear un diccionario de vuestras películas/obras favoritas (clave: autor, valor:película)
diccionario = {"Clint Eastwood" : "The Unforgiven", "Stanley Kubrick" : "A Clockwork Orange", "Alex de la Iglesia" : "El día de la Bestia",
               "Berlanga" : "La escopeta nacional" , "Bajo Ulloa" : "Airbag"}

#Crear sentencia para imprimir por pantalla todo el diccionario.
print(diccionario.items())

#Crear sentencia para imprimir por pantalla sólo las claves del diccionario
print(diccionario.keys())

#Crear sentencia para imprimir por pantalla sólo los valores del diccionario.
print(diccionario.values())