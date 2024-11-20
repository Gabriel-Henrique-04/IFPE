# Solicita as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média aritmética
media = (nota1 + nota2) / 2

# Determina a mensagem com base na média
if 0.0 <= media < 3.0:
    mensagem = "Reprovado"
elif 3.0 <= media < 7.0:
    mensagem = "Exame"
elif 7.0 <= media <= 10.0:
    mensagem = "Aprovado"
else:
    mensagem = "Média inválida"

# Mostra a média e a mensagem correspondente
print(f"Média: {media:.2f}")
print(f"Mensagem: {mensagem}")
