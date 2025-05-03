"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

vbc-shqr-wxd (Meet)

- Problema:
- Analise o resultado de uma transação comercial. Verifique a situação final
do comerciante trabalhando com os valores lidos, ou seja, o preço de compra
e o preço de venda. Gere a tela de saída com uma das seguintes mensagens:
“Teve lucro.”, “Teve prejuízo.” ou “Os valores são iguais.”.

- Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Testes (se ...)
Saída de dados (escreva)

Teste 1: Entrada: compra = 1000, venda = 1200     Saída: Teve lucro.
Teste 2: Entrada: compra = 1200, venda = 1000     Saída: Teve prejuízo.
Teste 3: Entrada: compra = 1000, venda = 1000     Saída: Os valores são iguais.
"""



# Recebe os valores de compra e de venda
# Lê o valor, converte para float e atribui à variável
vl_compra = float(input("Preço de compra: "))
vl_venda = float(input("Preço de venda: "))

if vl_venda > vl_compra:
    print("Teve lucro.")
elif vl_compra > vl_venda:
    print("Teve prejuízo.")
else:
    print("Os valores são iguais.")
''' --- Alterações:
a. Na tela de saída, mostre também o valor do preço de compra e 
   do preço de venda.
b. Peça para o usuário digitar também o nome do produto.
c. Mostre o nome do produto na tela de saída.

'''
