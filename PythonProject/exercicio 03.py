ct = 0
soma = 0
while True:
    num1 = int(input("Digite um numero:"))
    if num1 == 0:
     break
    elif num1%2 == 0:
     ct += 1
     soma += num1
     media = soma/ct
print(f"media: {media:.4f}\nForam digitados {soma} e {ct} sao pares ")

