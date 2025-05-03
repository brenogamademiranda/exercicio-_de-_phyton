# Função para somar
def somar(x, y):
    return x + y

# Função para subtrair
def subtrair(x, y):
    return x - y

# Função para multiplicar
def multiplicar(x, y):
    return x * y

# Função para dividir
def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

# Função principal
def calculadora():
    print("Selecione a operação desejada:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Receber a escolha do usuário
    operacao = input("Digite o número da operação (1/2/3/4): ")

    # Verificar se o usuário inseriu um número válido
    if operacao in ['1', '2', '3', '4']:
        # Solicitar números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            print(f"{num1} + {num2} = {somar(num1, num2)}")

        elif operacao == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")

        elif operacao == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        elif operacao == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")

    else:
        print("Operação inválida!")

# Chamar a função principal para rodar a calculadora
calculadora()



