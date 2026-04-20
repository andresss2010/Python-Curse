#creando una lista (list) (se pueden modificar los elementos, se accede por índice, se pueden repetir los elementos y tienen orden)
lista = ["andres", "ramos", 15, 175, True]

#creando una tupla (tuple) (no se pueden modificar los elementos, se accede por índice, tienen orden, se pueden repetir los elementos)
tupla = ("daniela", "valle", 14, 160, False)

#esto es valido porque las listas son mutables y se pueden modificar los elementos
lista[0] = "juan"

#esto no se puede hacer porque las tuplas son inmutables y no se pueden modificar los elementos
#tupla[0] = "maria" 


#creando un conjunto (set) (no se pueden modificar los elementos, no tienen orden, no se accede por índice, no permiten duplicados)
conjunto = {"andres", "ramos", 15, 175, True, 'andres'} 

#esto no se puede hacer porque los conjuntos no tienen orden y no se accede por índice
#print(conjunto[2]) 

#creando un diccionario (dict) la estructura es key:value y separamos con comas.
#(se pueden modificar los elementos, no tienen orden, se accede por clave, no permiten claves duplicadas)
diccionario = {
    "nombre": "andres",
    "apellido" : "ramos",
    "edad" : 15,
    "estatura" : 1.75,
    "esta feliz" : True,
    'edad': 16
}

diccionario['nombre'] = 'daniela' #esto es valido porque los diccionarios son mutables y se pueden modificar los elementos

print(diccionario["edad"] + 2)  


#EJERCICIOS DIA 2

#Crea una lista con tus 5 comidas favoritas. Modifica la tercera.

comida_fav = ["pizza", "hamburguesa", "tacos", "burritos", "lasaña"]
comida_fav[2] = "sushi"
print(comida_fav)

#Crea un diccionario que represente un auto (marca, modelo, año).

carro = {
    'marca' : 'bmw',
    'modelo' : 'm4',
    'año' : 2025
}