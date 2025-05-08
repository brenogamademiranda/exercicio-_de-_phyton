def main():
    soma_pares = soma_impares = 0
    qtd_pares = qtd_impares = 0
    print("Digite números inteiros (0 para sair):")
    while True:
        try:
            numero = int(input("Número: "))

            if numero == 0:
                break

            if numero % 2 == 0:
                soma_pares += numero
                qtd_pares += 1
            else:
                soma_impares += numero
                qtd_impares += 1
        except ValueError:
            print("insira um número inteiro válido.")

    media_pares = soma_pares / qtd_pares if qtd_pares > 0 else 0
    media_impares = soma_impares / qtd_impares if qtd_impares > 0 else 0
    print("\nResultados:")
    print(f"Média dos números pares: {media_pares:.2f}")
    print(f"Média dos números ímpares: {media_impares:.2f}")
if __name__ == "__main__":
    main()