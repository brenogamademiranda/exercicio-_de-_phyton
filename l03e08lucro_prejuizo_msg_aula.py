
vl_compra = float(input("Preço de compra: "))
vl_venda = float(input("Preço de venda: "))

if vl_venda > vl_compra:
    print("Teve lucro.")
elif vl_compra > vl_venda:
    print("Teve prejuízo.")
else:
    print("Os valores são iguais.")
