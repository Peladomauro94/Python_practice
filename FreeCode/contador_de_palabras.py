"""
Preguntamos al usuario en que está pensando. Cuando se introduce la respuesta, 
realizará el conteo de palabras en la sentencia e imprimimos en la salida el resultado.

Ejemplo:

Pregunta: ¿En qué estás pensando?

Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto
 pa
Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!

Para llevar esto a cabo, vamos a crear un fichero de texto y añadimos una unas frases, 
y contamos cuántas palabras tiene y lo imprimimos.

"""

 
frase = (input("¿En qué estás pensando?"))
if frase != "":
    frase_lista = frase.split()
    cantidad_palabras = len(frase_lista)
    print(cantidad_palabras)
    
print(f"¡Muy bien, tu me has mostrado tu pensamiento en {cantidad_palabras} palabras!")
