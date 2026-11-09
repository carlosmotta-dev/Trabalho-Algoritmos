#Algoritmo de ordenacao que:
#1- Procura o menor número da lista.
#2- Troca esse número com o primeiro elemento.
#3- Procura o menor número entre os elementos restantes.
#4- Troca com o segundo elemento.
#5- Repete até a lista estar ordenada.
#Complexidade o(n²) no melhor no médio e no pior caso.
#Poucas linhas de codigo, facilita na implementacao.
#Percorre a lista muitas vezes, por isso não é indicado em listas grandes.


import random
import time

num = []

for i in range(100000):
    num.append(random.randint(1, 100000))

def selection_sort(lista):
    total = len(lista)

    for p_list in range(total):
        menor = p_list
        for s_list in range(p_list + 1, total):
            if lista[s_list] < lista[menor]:
                menor = s_list

        lista[p_list], lista[menor] = lista[menor], lista[p_list]

    return lista

print("Iniciando ordenacao...")

inicio = time.time()

selection_sort(num)

fim = time.time()

print("Ordenacao concluida!")
print(num[:20])
print("Tempo:", fim - inicio, "segundos")