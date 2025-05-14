ct = 0
soma = 0
print("digite [-1] para sair a repetição")
while True:
    numero = int(input("digite um numero:"))
    if numero == -1:
        break
    ct += 1
    soma += numero
print(f" quantidades de numeros digitados {ct} e a soma e igual {soma}")