numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Verifica se os números são múltiplos entre si
if numero1 % numero2 == 0 or numero2 % numero1 == 0:
    print("sim")
else:
    print("não")