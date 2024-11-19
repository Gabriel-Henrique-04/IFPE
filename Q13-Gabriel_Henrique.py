l = int(input("Digite a quantidade de linhas: "))
c = int(input("Digite a quantidade de colunas: "))

for n in range(l):
    for c in range(c+1):
        print("#", end="")
    print()