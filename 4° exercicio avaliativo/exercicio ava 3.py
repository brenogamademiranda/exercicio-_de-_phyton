soma = 0
quantidade = 0

for numero in range(1,11):
    dobro = numero * 2
    print(dobro)
    soma += dobro
    quantidade += 1

media = soma / quantidade

print(f"soma dos numeres = {soma} e a media = {media}")