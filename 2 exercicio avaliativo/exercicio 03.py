a = int(input("Digite o 1° valor:"))
b = int(input("Digte o 2° valor:"))
c = int(input("Digite o 3° valor:"))

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
     maior = c

print(f"O maior valor e: {maior}")


