
vl_compra = float(input("Preço de compra: "))
vl_venda = float(input("Preço de venda: "))

transacao = vl_venda - vl_compra      # calcula o lucro da venda

if transacao > 0:    # Se venda > compra, houve lucro
    print("A transação teve lucro de R$", transacao)
elif transacao < 0:  # Se venda < compra, ou seja, houve prejuízo
    print(f"A transação teve prejuízo de R${-transacao}")  # Multiplica por -1
else:                # Se venda = compra, não houve lucro ou prejuízo
    print("A transação não resultou em lucro nem prejuízo.")

