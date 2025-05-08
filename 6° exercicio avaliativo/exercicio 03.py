def somar_tres_valores(a, b, c):
    return a + b + c

def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    resultado = somar_tres_valores(num1, num2, num3)
    print("Soma dos três valores:", resultado)

main()
