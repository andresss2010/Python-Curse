#definiendo una variable
a = 2
b = 8
c = a + b

#definiendo una variable con camelCase
nombreCompleto = "andres"

#definiendo una variable con snake_case
nombre_completo = "andres ramos"


numero = 15
numero += 5


#concatenar (unir) con +
user = "andres"
bienvenida = 'Hola ' + user + " como estas?"


#concatenar con f-strings
name = 'andres'
welcome = f"Hola {name} como estas?"

#operadores de pertenencia (in / not in)
print("andres" in bienvenida) #true
print("andres" not in bienvenida) #false


#EJERCICIOS

#1.Crea un programa que guarde tu nombre, tu edad y tu estatura en variables y los imprima en pantalla.
nombre = "andres"
edad = "15"
estatura = "175"

msg = f"hola {nombre}, tienes {edad} años y mides {estatura}cm, pasa adelante!"

#2. Define una variable con un valor booleano que indique si estás emocionado por aprender Python.

feliz = True

feeling = f"me siento feliz de aprender python? {feliz}"
print(feeling)

# EJERCICIOS DÍA 1 REVISADOS

# 1. Variables con tipos de datos correctos
nombre = "andres"
edad = 15          # Ahora es un número entero
estatura = 175     # Ahora es un número entero

msg = f"hola {nombre}, tienes {edad} años y mides {estatura}cm, pasa adelante!"
print(msg)

# 2. Variable booleana
esta_emocionado = True  # Usando snake_case para el nombre

feeling = f"me siento feliz de aprender python? {esta_emocionado}"
print(feeling)
