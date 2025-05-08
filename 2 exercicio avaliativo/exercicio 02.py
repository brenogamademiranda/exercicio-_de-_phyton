a = int(input("Digite o 1° valor:"))
b = int(input("Digte o 2° valor:"))
c = int(input("Digite o 3° valor:"))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print(f" O maior valor é: {maior}")