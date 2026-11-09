#Algoritmo de ordenacao que:
#1- Escolhe um elemento da lista como pivo.
#2- Compara os demais elementos com o pivo.
#3- Coloca os menores elementos a esquerda do pivo.
#4- Coloca os maiores elementos a direita do pivo.
#5- Repete o processo nas duas partes ate que a lista esteja ordenada.
#Complexidade O(n log n) no melhor e no caso medio, O(n²) no pior caso.
#Muito eficiente na pratica e indicado para listas grandes.
#Pode ficar mais lento quando o pivo divide a lista de forma muito desigual.


import random
import time

num = []

for i in range(100000):
    num.append(random.randint(1, 100000))

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[-1]

    menores = []
    maiores = []
    iguais = []

    for elemento in lista:
        if elemento < pivo:
            menores.append(elemento)

        elif elemento > pivo:
            maiores.append(elemento)

        else:
            iguais.append(elemento)

    return quick_sort(menores) + iguais + quick_sort(maiores)

print("Iniciando ordenacao...")

inicio = time.time()

num = quick_sort(num)

fim = time.time()

print("Ordenacao concluida!")
print(num[:20])
print("Tempo:", fim - inicio, "segundos")