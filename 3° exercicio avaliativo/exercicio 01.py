def main():
    print("Bem-vindo ao analisador de números reais!")
    print("Digite os números que desejar e, quando quiser parar, digite 'sair'.")
    valores = []
    while True:
        entrada = input("Digite um número (ou 'sair' para finalizar): ")

        if entrada.lower() == 'sair':
            break

        try:
            numero = float(entrada)
            valores.append(numero)
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")
    if valores:
        quantidade = len(valores)
        soma = sum(valores)
        media = soma / quantidade
        maiores_que_20 = sum(1 for valor in valores if valor > 20)

        print("\n===== RESULTADOS =====")
        print(f"Quantidade de valores digitados: {quantidade}")
        print(f"Soma dos valores digitados: {soma:.2f}")
        print(f"Média aritmética: {media:.2f}")
        print(f"Quantidade de valores maiores que 20: {maiores_que_20}")
    else:
        print("Nenhum número foi digitado.")

    print("Obrigado por usar o programa! Até a próxima.")
if __name__ == "__main__":
    main()
