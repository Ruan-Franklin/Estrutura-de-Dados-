"""
Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão
"""

def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def divisao(a, b):
    return a/b

def multiplicacao(a, b):
    return a*b

num1 = int(input(("Digite o primeiro número inteiro: ")))
num2 = int(input(("Digite o segundo número inteiro: ")))

print("A soma entre os inteiros é: ", soma(num1, num2))
print("A subtração entre os inteiros é: ", subtracao(num1, num2))
print("A multiplicação entre os inteiros é: ", multiplicacao(num1, num2))
print("A divisão entre os inteiros é: ", divisao(num1, num2))