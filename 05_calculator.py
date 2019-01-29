#Crear las sentencias necesarias para recoger dos números a través del terminal
operando1 = int(input("introduce el primer operando... "))
operando2 = int(input("introduce el segundo operando... "))

#Integrar funcionalidades de suma, multiplicación, división, y exponencial
#Permitir escoger el modo de operación de forma manual (el usuario ha de introducir un número para que sepa qué operación realizar)
#Realizar las operaciones e imprimir el valor por pantalla.
operacion = int(input("Introduzca la operación a realizar: 1 = suma, 2 = multiplicación, 3 división y 4 exponencial... "))
if operacion == 1:
    resultado = operando1 + operando2
    signo = "+"
    print(operando1, signo, operando2, " = ", resultado)
elif operacion == 2:
    resultado = operando1 * operando2
    signo = "x"
    print(operando1, signo, operando2, " = ", resultado)
elif operacion == 3:
    resultado = operando1 / operando2
    signo = "/"
    print(operando1, signo, operando2, " = ", resultado)
elif operacion == 4:
    resultado = operando1 ** operando2
    signo = "^"
    print(operando1, signo, operando2, " = ", resultado)
else:
    print("operación no disponible")
#Subir el archivo a vuestra cuenta de GitHub