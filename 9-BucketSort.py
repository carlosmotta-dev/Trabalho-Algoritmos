#Algoritmo de ordenacao que:
#1- Identifica o menor e o maior numero da lista.
#2- Cria varios baldes para distribuir os elementos.
#3- Coloca cada numero no balde correspondente ao seu valor.
#4- Ordena os elementos dentro de cada balde.
#5- Junta todos os baldes em uma unica lista ordenada.
#Complexidade O(n + k) no melhor caso e no caso medio e O(n²) no pior caso.
#Bom quando os elementos estao distribuidos de maneira uniforme.
#Pode apresentar baixo desempenho quando muitos elementos ficam em um unico balde.


import random
import time

num = []

for i in range(100000):
    num.append(random.randint(1, 100000))

def bucket_sort(lista):
    if len(lista) <= 1:
        return lista

    menor = min(lista)
    maior = max(lista)

    quantidade = 10
    baldes = [[] for _ in range(quantidade)]

    for p_lista in lista:
        indice = int((p_lista - menor) / (maior - menor + 1) * quantidade)
        baldes[indice].append(p_lista)

    resultado = []

    for s_lista in baldes:
        s_lista.sort()
        resultado.extend(s_lista)

    return resultado

print("Iniciando ordenacao...")

inicio = time.time()

num = bucket_sort(num)

fim = time.time()

print("Ordenacao concluida!")
print(num[:20])
print("Tempo:", fim - inicio, "segundos")