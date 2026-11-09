#Algoritmo de ordenacao que:
#1- Compara dois numeros vizinhos da lista.
#2- Se o primeiro for maior que o segundo, troca suas posicoes.
#3- Continua comparando os numeros seguintes.
#4- Ao final de cada passada, o maior numero vai para o final da lista.
#5- Repete o processo ate a lista estar ordenada.
#Complexidade O(n²) no pior e no caso medio, O(n) no melhor caso (com verificacao de trocas).
#Facil implementacao e bom para entender algoritmos de ordenacao.
#Realiza muitas comparacoes e trocas, por isso nao é indicado em listas grandes.


import random
import time

num = []

for i in range(100000):
    num.append(random.randint(1, 100000))

def bubble_sort(lista):
    total = len(lista)

    for p_list in range(total):
        for s_list in range(total - 1 - p_list):

            if lista[s_list] > lista[s_list + 1]:
                lista[s_list], lista[s_list + 1] = lista[s_list + 1], lista[s_list]

    return lista

print("Iniciando ordenacao...")

inicio = time.time()

bubble_sort(num)

fim = time.time()

print("Ordenacao concluida!")
print(num[:20])
print("Tempo:", fim - inicio, "segundos")