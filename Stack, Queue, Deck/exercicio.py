"""


Durante as aulas você aprendeu que o Bubble Sort é o algoritmo mais lento, enquanto que o Quick Sort e Merge Sort tem a tendência a serem mais rápidos. Para testar se efetivamente teremos resultados mais rápidos, siga o seguinte roteiro:
Crie um vetor com 5000 números (do tipo float) aleatórios entre 0 e 1 (utilize a biblioteca random)
Use o comando %timeit para medir o desempenho e compare o tempo de execução de cada algoritmo
Lembre de utilizar o mesmo vetor em todos os experimentos!
"""
import random
import timeit
import time
import numpy as np


def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor

def merge_sort(vetor):
    if len(vetor) > 1:
        meio = len(vetor) // 2
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
    return vetor


def particao(vetor, inicio, fim):
    pivo = vetor[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    return i + 1

def quick_sort(vetor, inicio, fim):
    if inicio < fim:
        pi = particao(vetor, inicio, fim)
        quick_sort(vetor, inicio, pi - 1)
        quick_sort(vetor, pi + 1, fim)
    return vetor



# Gerar vetor com 5000 números aleatórios entre 0 e 1
vetor = [random.random() for _ in range(5000)]
vetor_bubble = vetor.copy()
vetor_merge = vetor.copy()
vetor_quick = vetor.copy()

# Medir tempo de execução do Bubble Sort
start_time = time.time()
bubble_sort(vetor_bubble)
end_time = time.time()
print(f"Tempo de execução do Bubble Sort: {end_time - start_time:.6f} segundos")
merge_sort(vetor_merge)
start_time = time.time()
merge_sort(vetor_merge)
end_time = time.time()
print(f"Tempo de execução do Merge Sort: {end_time - start_time:.6f} segundos")
start_time = time.time()
quick_sort(vetor_quick, 0, len(vetor_quick) - 1
)
end_time = time.time()
print(f"Tempo de execução do Quick Sort: {end_time - start_time:.6f} segundos")