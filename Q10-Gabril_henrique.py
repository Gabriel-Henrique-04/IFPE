primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
cal = int(input("Qual a operação que você deseja fazer? \n Digite 1 para o primeiro número ser elevado ao segundo \n Digite 2 para a soma dos quadrados de cada um dos números \n Digite 3 para a soma das raízes quadradas de cada um dos números "))


match cal:
    case 1:
        print(f"O resultado do primeiro número elevado ao segundo é: {(primeiro**segundo):.1f}")

    case 2:
        print(f"A soma dos quadrados de cada um dos números: {((primeiro**2)+(segundo**2)):.1f}")

    case 3:
        print(f"A soma das raízes quadradas de cada um dos números: {(primeiro**(1/2))+(segundo**(1/2)):.1f}")

    case _:
        print("ERRO")