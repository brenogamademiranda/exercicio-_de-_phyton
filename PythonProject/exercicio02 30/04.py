def mostrar_valor1(valor1):
 dobro = valor1*2
 return dobro
def mostrar_valor2(valor2):
 triplo = valor2*3
 return triplo
if __name__== "__main__":
    valor= int(input("valor inteiro:"))
    v_retornado1 = mostrar_valor1(valor)

    print(f"\n o resultado{v_retornado1}")

    valor__2= int(input("valor inteiro:"))
    v_retornado2 = mostrar_valor2(valor__2)
    print(f"o resultado {v_retornado2}")
