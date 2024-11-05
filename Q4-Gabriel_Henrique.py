x1 = float(input("Informe o valor X1: "))
y1 = float(input("Informe o valor de Y1: "))
x2 = float(input("Informe o valor de X2: "))
y2 = float(input("Informe o valor de Y2: "))

r = pow((x2 - x1), 2) + pow((y2 - y1), 2)

r2 = r ** 0.5

print("O resultado da distância é: {:.3f} ".format(r2))