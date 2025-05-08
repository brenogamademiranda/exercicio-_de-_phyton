
valor_inicial = float(input("Digite o valor inicial em Fahrenheit: "))
valor_final = float(input("Digite o valor final em Fahrenheit: "))

print("\nFahrenheit | Celsius")
print("---------------------")

if valor_inicial <= valor_final:
    for f in range(int(valor_inicial), int(valor_final) + 1):
        c = 5 * (f - 32) / 9
        print(f"   {f:.1f} ºF  | {c:.3f} ºC")

else:
    for f in range(int(valor_inicial), int(valor_final) - 1, -1):
        c = 5 * (f - 32) / 9
        print(f"   {f:.1f} ºF  | {c:.3f} ºC")
