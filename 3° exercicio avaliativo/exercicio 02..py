def main():
    aprovados = 0
    reprovados = 0
    total_alunos = 0
    print("Digite as notas dos alunos (digite um valor negativo para encerrar):")
    while True:
        try:
            nota = float(input("Nota do aluno: "))

            if nota < 0:
                break

            total_alunos += 1
            if nota >= 5:
                aprovados += 1
            else:
                reprovados += 1
        except ValueError:
            print("insira um número válido.")

    print("\nResultados:")
    print(f" alunos que fizeram a prova: {total_alunos}")
    print(f" alunos aprovados: {aprovados}")
    print(f" alunos reprovados: {reprovados}")
if __name__ == "__main__":
    main()