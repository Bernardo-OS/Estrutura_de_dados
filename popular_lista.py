
lista = [2,5,8,4,67,9,1,0,4,3,2,6,3,5,6,4,9,6,235]
lista_pares = []
lista_impares = []
replicados_pares = 0
replicados_impares = 0

def separaParesEImpares(lista):
    global replicados_pares, replicados_impares
    for i in lista:
        if(i % 2 == 0):
            if(i not in lista_pares):
                 lista_pares.append(i)
            else:
                replicados_pares=replicados_pares+1

        else:       
            if(i not in lista_impares):
                lista_impares.append(i)
            else:
                replicados_impares=replicados_impares+1

separaParesEImpares(lista)
print("Numeros repitidos impares:")
print(replicados_impares)
print(lista_impares)
print("Numeros repitidos pares:")
print(replicados_pares)
print(lista_pares)