ct = 0
soma = 0
disciplina = int(input(" digite o nome da disciplina:"))
while True:
    nota = float(input("digite o numero:"))
    if nota == -1:
        break
    ct += 1
    soma += nota
    media = soma/9
print(f"disciplina: {disciplina} \nmedia: {media:.2f} \nquantidade de alunos: {ct}")