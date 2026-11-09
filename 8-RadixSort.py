#Algoritmo de ordenacao que:
#1- Identifica a quantidade de digitos do maior numero da lista.
#2- Comeca ordenando os numeros pelo digito menos significativo (unidades).
#3- Organiza os numeros de acordo com o digito analisado.
#4- Repete o processo para todas casas decimais.
#5- Continua ate que todos os digitos tenham sido analisados.
#6- Finaliza com a lista completamente ordenada.
#Complexidade O(d * (n + k)) no melhor, no medio e no pior caso.
#Eficiente para listas grandes de numeros inteiros com quantidade limitada de digitos.
#Pode consumir memoria adicional e apresentar baixo desempenho com numeros que possuem muitos digitos.


import random
import time

num = []

for i in range(100000):
    num.append(random.randint(1, 100000))

def counting_sort(lista, exp):
    total = len(lista)

    resultado = [0] * total
    contagem = [0] * 10

    for p_lista in range(total):
        digito = (lista[p_lista] // exp) % 10
        contagem[digito] += 1

    for s_lista in range(1, 10):
        contagem[s_lista] += contagem[s_lista - 1]

    for t_lista in range(total - 1, -1, -1):
        digito = (lista[t_lista] // exp) % 10
        resultado[contagem[digito] - 1] = lista[t_lista]
        contagem[digito] -= 1

    for q_lista in range(total):
        lista[q_lista] = resultado[q_lista]


def radix_sort(lista):
    maior = max(lista)
    exp = 1

    while maior // exp > 0:
        counting_sort(lista, exp)
        exp *= 10

    return lista

print("Iniciando ordenacao...")

inicio = time.time()

num = radix_sort(num)

fim = time.time()

print("Ordenacao concluida!")
print(num[:20])
print("Tempo:", fim - inicio, "segundos")