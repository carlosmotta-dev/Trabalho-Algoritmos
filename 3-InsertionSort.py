#Algoritmo de ordenacao que:
#1- Considera o primeiro elemento da lista como ordenado.
#2- Pega o proximo elemento da lista.
#3- Compara esse elemento com os anteriores.
#4- Desloca os elementos maiores uma posicao para a direita.
#5- Insere o elemento na posicao correta.
#6- Repete o processo ate a lista estar ordenada.
#Complexidade O(n²) no pior e no caso medio, O(n) no melhor caso.
#Bom para listas pequenas ou quase ordenadas.
#Faz muitas comparacoes e deslocamentos, por isso nao é indicado para listas grandes.


import random
import time

num = []

for i in range(100000):
    num.append(random.randint(1, 100000))

def insertion_sort(lista):
    total = len(lista)

    for p_list in range(1, total):
        atual = lista[p_list]
        s_list = p_list - 1

        while s_list >= 0 and lista[s_list] > atual:
            lista[s_list + 1] = lista[s_list]
            s_list -= 1

        lista[s_list + 1] = atual

    return lista

print("Iniciando ordenacao...")

inicio = time.time()

insertion_sort(num)

fim = time.time()

print("Ordenacao concluida!")
print(num[:20])
print("Tempo:", fim - inicio, "segundos")