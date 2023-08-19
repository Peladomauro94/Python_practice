"""
EL FAMOSO "FIZZBUZZ"

Escribe un programa que muestre por consola (con un print) los
numeros de 1 a 100 (ambos incluidos y con un salto de linea entre
cada imporesion), sustituyendo los siguientes:
- Multiplos de 3 por la palabra "fizz"
- Multiplos de 5 por la palabra "buzz"
- Multiplos de 3 y 5 a la vez por la plabra "fizzbuzz"

"""

def fizzbuzz():
    for index in range(100):
        number = index + 1
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(index)
        
fizzbuzz()

"""

    ¿ES O NO UN ANAGRAMA?

    Escribe una funcion que reciba dos palbras (String) y retorne
    verdadero o falso (Bool) segun sean o no anagramas.
    Un anagrama consiste ene formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
    No hace falta comprobar que ambas palabras existan.
    Dos palabras exacramente iguales no son anagrama.
 
"""

def anagrama(palabra1, palabra2):
    
    if palabra1.lower() == palabra2.lower():
        return False
    elif sorted(palabra1.lower()) == sorted(palabra2.lower()):
        return True
    else:
        return False

print(anagrama("amor", "roma"))


"""

Escribe un programa que imporima los 50 primero numeros de la sucesion 
de Fibonacci empezando de 0.
La serie Fibonacci se compone por una sucesion de numeros en la que el
siguiente siempre es la suma de ls dos anteriores.

0, 1, 1, 2, 3, 5, 8, 13....

"""

def fibonacci ():
    
    previous=0
    next=1

    for index in range(50):
        print(previous)
        fib = previous + next
        previous = next
        next = fib
     

fibonacci()


"""

    ¿ES UN NUMERO PRIMO?
    Escribe un programa que se encargue de comprobar si un numero es o no primo.
    Hecho esto, imprime los numeros prios entre 1 y 100.

    
"""


def primo ():

    for numero in range (1, 101):

        if numero >= 2:

            is_divisible = False

            for index in range(2, numero):
                if numero % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(numero)
            
primo()


"""
    INVIRTIENDO CADENAS

    crea un programa que invierta el orden de una cadena de texto 
    sin usar funciones propias del lenguaje que lo hagan de forma automática.
    - Si le pasamos "hola mundo" nos retornaría "odnm aloh"
"""

def reverse(text):
    texto = ""
    texto_length = len(text)
    for index in range(0, texto_length):
        texto += text[texto_length - index - 1]
    return texto



print(reverse("hola mundo"))