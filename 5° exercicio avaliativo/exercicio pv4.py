# Inicializa a variável de soma
soma = 0

for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero

print(f"A soma dos números ímpares e múltiplos de 3 de 1 a 500 é: {soma}")
