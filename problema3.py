#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
t = input().split()

def arbolTrinario(numero):
    return [numero, [], [], []] 

def insertaEnArbolTrinario(arbol,numero):
    if arbol==[]:
        arbol+=arbolTrinario(numero)
    elif int(numero) < int(arbol[0]):
        insertaEnArbolTrinario(arbol[1],numero)
    elif int(numero) == int(arbol[0]):
        insertaEnArbolTrinario(arbol[2],numero) 
    else:
        insertaEnArbolTrinario(arbol[3],numero)


w = arbolTrinario(int(t[0]))

for i in range(1, len(t)):
    insertaEnArbolTrinario(w, int(t[i]))

print(w)