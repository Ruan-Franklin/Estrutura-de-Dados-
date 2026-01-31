"""
Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
- Se a média for maior do que 6.0, o aluno está aprovado
- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado
"""

def calcular_media(n1, n2, n3):
    pegou_exame = False
    media = (n1 + n2 + n3) / 3
    if media >= 0.0 and media <= 4.0:
        return media, "Reprovado"

    elif media >= 4.1 and media <= 6.0:
        pegou_exame = True
        return media, "Exame"

    else:
        return media, "Aprovado"

nota1 = float(input("Digite a nota M1: "))
nota2 = float(input("Digite a nota M2: "))
nota3 = float(input("Digite a nota M3: "))
media, status = calcular_media(nota1, nota2, nota3)
print(f"Média: {media:.2f} - Status: {status}")
if status == "Exame":
    nota_exame = float(input("Digite a nota do exame: "))
    if nota_exame >= 6.0:
        status = "Aprovado"
    else:
        status = "Reprovado"
    print(f"Status final após exame: {status}!", "Média do exame: " f'{nota_exame:.2f}')

