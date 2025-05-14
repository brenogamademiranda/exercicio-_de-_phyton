masculino = 0
feminino = 0
maioraltura = -99999
menoraltura = 999999
ct = 0
soma = 0

print("para sair do loop utilize o valor [0]")
while True:
    genero = input("Digite o seu endereço (M/F)")
    if genero == '0':
        break
    if genero == 'F':
        feminino+=1
    if genero == 'M':
        masculino+=1

    altura = float(input("digite sua altura "))
    if altura == 0:
        break
    if altura>maioraltura:
        maioraltura=altura
    if altura<menoraltura:
        menoraltura=altura
        ct+= 1
        soma += altura
        soma = soma/ct
print(f"maior altura: {maioraltura} e menor altura: {menoraltura} masculino: {masculino} feminino: {feminino} \n ct {ct}  soma {soma}")