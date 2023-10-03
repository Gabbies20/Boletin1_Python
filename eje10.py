#Crea una lista de números y calcula su promedio.


"""_summary_
lista = [7,8,10,7,6,8,9,10]
longitud_lista = len(lista)
suma = 0

for i in lista:
    suma += i
    print(i)

promedio = suma / longitud_lista
print(f"El promedio es {promedio}")
    """
# Crear una lista de números
numeros = [7,8,10,7,6,8,9,10]

# Calcular la suma de los números en la lista
suma = sum(numeros)

# Calcular la cantidad de números en la lista
cantidad = len(numeros)

# Calcular el promedio
promedio = suma / cantidad

# Imprimir el promedio
print("La lista de números es:", numeros)
print("El promedio de los números en la lista es:", promedio)

