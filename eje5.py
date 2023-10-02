#Calcular el factorial de un número:

n = 5
suma = 1

for i in reversed(range(1,n+1)):
    suma *= i
print(suma)