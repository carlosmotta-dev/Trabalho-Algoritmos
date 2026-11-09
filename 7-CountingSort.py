#Algoritmo de ordenacao que:
#1- Identifica o menor e o maior numero da lista.
#2- Cria uma segunda lista para contar a quantidade de vezes que cada numero aparece.
#3- Percorre a lista original contando as ocorrencias de cada numero.
#4- Organiza as contagens para determinar a posicao correta de cada elemento.
#5- Reconstrói a lista original em ordem crescente.
#Complexidade O(n + k) no melhor, no medio e no pior caso.
#Muito eficiente para listas grandes com valores inteiros dentro de uma faixa limitada.
#Pode consumir muita memoria quando a diferenca entre o menor e o maior valor é muito grande.


import random
import time

num = []

for i in range(100000):
    num.append(random.randint(1, 100000))

def counting_sort(lista):

    maior = max(lista)
    menor = min(lista)

    contagem = [0] * (maior - menor + 1)

    for p_lista in lista:
        contagem[p_lista - menor] += 1

    resultado = []

    for s_lista in range(len(contagem)):
        for t_lista in range(contagem[s_lista]):
            resultado.append(s_lista + menor)

    return resultado

print("Iniciando ordenacao...")

inicio = time.time()

num = counting_sort(num)

fim = time.time()

print("Ordenacao concluida!")
print(num[:20])
print("Tempo:", fim - inicio, "segundos")