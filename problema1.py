#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t = input().split()
m = input().split()

print(t)

for i in range(len(t)):
    if t[i].isnumeric():
        t[i] = int(t[i])

for i in range(len(m)):
    if m[i].isnumeric():
        m[i] = int(m[i])

print(m + t + m)
