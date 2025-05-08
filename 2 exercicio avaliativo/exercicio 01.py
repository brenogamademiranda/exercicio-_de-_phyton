a = int(input("Digite o 1° valor:"))
b = int(input("Digite o 2° valor:"))

if a>b:
 a, b = b, a
print(f" Valores em ordem crescente: {a}, {b}")