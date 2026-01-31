"""
Leia a idade do usuário e classifique-o em:
- Criança – 0 a 12 anos
- Adolescente – 13 a 17 anos
- Adulto – acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida
"""

def calcular_idade(idade):
    if idade < 0:
        return "Essa idade é inválida."
    elif idade >= 0 and idade <= 13:
        return "Criança"
    elif idade >= 13 and idade <= 17:
        return "Adolescente"
    else:
        return "Adulto"


idade = int(input("Digite a sua idade: "))
classificacao = calcular_idade(idade)
print("Classificação: ", classificacao)