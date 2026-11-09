#Algoritmo de ordenacao que:
#1- Organiza os elementos em uma estrutura de arvore chamada Heap.
#2- Coloca o maior elemento na raiz da arvore (Max Heap).
#3- Troca o maior elemento com o ultimo elemento da lista.
#4- Remove o ultimo elemento da estrutura, que ja esta na posicao correta.
#5- Reorganiza a arvore para manter a propriedade Max Heap.
#6- Repete o processo ate que a lista esteja ordenada.
#Complexidade O(n log n) no melhor, no medio e no pior caso.
#Bom para listas grandes e possui baixo consumo de memoria adicional.
#É mais complexo que algoritmos simples, como Bubble Sort e Selection Sort.


import random
import time

num = []

for i in range(100000):
    num.append(random.randint(1, 100000))

def heap_sort(lista):
    total = len(lista)

    def descer(p_lista, limite):
        maior = p_lista
        esquerda = 2 * p_lista + 1
        direita = 2 * p_lista + 2

        if esquerda < limite and lista[esquerda] > lista[maior]:
            maior = esquerda

        if direita < limite and lista[direita] > lista[maior]:
            maior = direita

        if maior != p_lista:
            lista[p_lista], lista[maior] = lista[maior], lista[p_lista]
            descer(maior, limite)

    for s_lista in range(total // 2 - 1, -1, -1):
        descer(s_lista, total)

    for t_lista in range(total - 1, 0, -1):
        lista[0], lista[t_lista] = lista[t_lista], lista[0]
        descer(0, t_lista)

    return lista

print("Iniciando ordenacao...")

inicio = time.time()

heap_sort(num)

fim = time.time()

print("Ordenacao concluida!")
print(num[:20])
print("Tempo:", fim - inicio, "segundos")