a = int(input("Digite o 1° lado:"))
b = int(input("Digite o 2° lado:"))
c = int(input("Digite o 3° lado:"))


if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("É um triângulo equilatero.")
    elif a == b or b == c or a == c:
        print("É um triângulo isosceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é um triângulo.")

