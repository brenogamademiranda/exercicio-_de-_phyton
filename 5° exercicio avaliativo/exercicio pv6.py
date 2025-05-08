
numero = int(input("Digite um número inteiro para ver sua tabuada: "))

for i in range(1, 11):
    resultado = i * numero
    print(f"{i}\tx\t{numero}\t=\t{resultado}")
