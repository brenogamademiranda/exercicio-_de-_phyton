def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))
    imc = calcular_imc(peso, altura)
    print("Seu IMC é:", round(imc, 2))

main()
