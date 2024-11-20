# Define o valor do salário mínimo
SALARIO_MINIMO = 1212.00

# Solicita o salário atual do colaborador
salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

# Calcula o percentual de aumento
if salario_atual <= SALARIO_MINIMO:
    percentual_aumento = 20  # Percentual para até 1 salário mínimo
else:
    percentual_aumento = 15  # Percentual para acima de 1 salário mínimo

# Calcula o valor do aumento e o novo salário
valor_aumento = salario_atual * (percentual_aumento / 100)
salario_reajustado = salario_atual + valor_aumento

# Mostra o resultado
print(f"Percentual de aumento: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Salário reajustado: R$ {salario_reajustado:.2f}")
