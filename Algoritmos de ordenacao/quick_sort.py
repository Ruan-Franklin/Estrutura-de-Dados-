import numpy as np

vetor = np.array([38, 27, 43, 3, 9, 82, 120])


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

vetor_ordenado = quick_sort(vetor, 0, len(vetor) - 1)
print(vetor_ordenado)