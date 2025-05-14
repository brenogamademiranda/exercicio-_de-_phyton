ct = soma = 0
for nota in range(1,6):
    nota = float(input("digite as notas:"))
    ct+=1
    soma += nota
media = soma/ct
print(f"as media são: {media}")
