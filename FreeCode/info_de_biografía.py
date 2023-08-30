"""

Pregunte a un usuario su información personal en una sola ronda de preguntas. 
Luego hay que verificar que la información que se ha ingresado sea válida. 
Finalmente, se imprime un resumen de toda la información que ha sido ingresada.

Por ejemplo: ¿Cuál es su nombre? Si el usuario ingresa *, 
hay que indicar que la entrada es incorrecta y se pide que se ingrese correctamente un nombre válido.


"""


nombre = input("Por favor ingrese su nombre.")

if len(nombre) < 3:
    nombre = input("Debe ingresar un nombre válido") 



fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento.")

if len(fecha_nacimiento.split()) < 3:
    print("Debe ingresar un fecha de nacimiento válida")
else:
    fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento.")



direccion = input("Por favor ingrese su direccion.")

if len(direccion) < 3:
    print("Debe ingresar una direccion válida")
else:
    direccion = input("Por favor ingrese su direccion.")


metas_personales = input("Por favor ingrese sus metas personales.")

if len(metas_personales.split()) < 3:
    print("Debe ingresar una meta personal valida")
else:
    metas_personales = input("Por favor ingrese sus metas personales.")