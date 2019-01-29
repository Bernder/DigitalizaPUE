#Crear un script en el que guardéis en una variable un número
numerico = int(input("Hola, introduce un número, por favor "))

#Controlar el tamaño del número en 4 rangos (menor de 20, entre 20 y 39, entre 40 y 59, mayor de 60)
#En cada uno de los casos imprimir por pantalla el número que se haya introducido.
if numerico < 20:
    print("Has introducido ", numerico, ", que es menor que 20")
elif numerico >= 20 and numerico < 40:
    print("Has introducido ", numerico, ", que está entre 20 y 39")
elif numerico >= 40 and numerico < 60:
    print("Has introducido ", numerico, ", que está entre 40 y 59")
else: print("Mayor de 60")