num1 = float(input("Digite o 1° numero:"))
num2 = float(input("Digite o 2° numero:"))

print("\nEscolha o sinal desejado")
print("+ -> Adição")
print("- ->Subtração")
print("* -> multiplicação")
print("/ -> Divisão")

sinal = input("digite o sinal desejado:")

if sinal == "+":
 resultado = num1 + num2
elif sinal == "-":
 resultado = num1 - num2
elif sinal == "*":
 resultado = num1 * num2
elif sinal == "/":
 resultado  = num1 / num2
print(f"Resultado: {resultado}")


