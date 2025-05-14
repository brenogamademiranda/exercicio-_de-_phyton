import random
ct=0
soma=0
print("numero sorteado:")
for numero in range(1,12):
    num_sorteado= random.randint(1,6)
    ct+=1
    soma += ct
    print(num_sorteado)
print(f"o valor{ct}")
print(f"o valor {soma}")