"""
Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

Ejemplo:

Mensaje que se muestra: ¿En qué número estás pensando?
Entrada: 25
Salida: ¡Es un número impar! ¿Puedes añadir otro?

"""

numero = int(input("Welcome! Please, enter a number from 1 to 1000"))

if numero > 0:
    if numero % 2 == 0:
        print("Es un numero par! ¿Puedes añadir otro?")
    else:
        print("Es un numero inpar! ¿Puedes añadir otro?")
else:
    print("El numero es igual o menor a 0")