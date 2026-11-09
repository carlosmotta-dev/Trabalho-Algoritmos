#Algoritmo de ordenacao que:
#1- Divide a lista em duas metades.
#2- Continua dividindo as metades em partes menores.
#3- Repete ate que cada parte tenha apenas um elemento.
#4- Junta as partes comparando os elementos em ordem crescente.
#5- Repete as juncoes ate formar uma unica lista ordenada.
#Complexidade O(n log n) no melhor, no medio e no pior caso.
#Muito eficiente para ordenar listas grandes.
#Utiliza memoria adicional para armazenar as partes durante a ordenacao.


import random
import time

num = []

for i in range(100000):
    num.append(random.randint(1, 100000))

def merge_sort(lista):

    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):

    resultado = []
    p_lista = 0
    s_lista = 0

    while p_lista < len(esquerda) and s_lista < len(direita):

        if esquerda[p_lista] <= direita[s_lista]:
            resultado.append(esquerda[p_lista])
            p_lista += 1

        else:
            resultado.append(direita[s_lista])
            s_lista += 1

    resultado.extend(esquerda[p_lista:])
    resultado.extend(direita[s_lista:])

    return resultado

print("Iniciando ordenacao...")

inicio = time.time()

num = merge_sort(num)

fim = time.time()

print("Ordenacao concluida!")
print(num[:20])
print("Tempo:", fim - inicio, "segundos")