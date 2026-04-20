
igual_que = 5 == 6

distinto_de = 5 != 6

mayor_que = 5 > 6

menor_que = 5 < 6

mayor_o_igual = 5 >= 6

menor_o_igual = 5 <= 6

#calculos combinados

a = 5
b = 10
c = 20
comparacion = a + b > c

#comparar usuarios
contraseña_almacenada = "DanielaRamos"
contraseña_ingresada = "DanielaRamos"

print(contraseña_almacenada == contraseña_ingresada)

#EJERCICIO DIA 2

#Realiza un programa que pida dos números al usuario y muestre si el primero es mayor que el segundo.

# Convertimos la entrada a entero inmediatamente
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

# Ahora la comparación es numérica y no de texto
print(num1, "es mayor que", num2, "?", num1 > num2)