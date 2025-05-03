"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema:
- Elabore o programa que faça a conversão de graus Fahrenheit (ºF) para
graus Celsius (ºC).
- Fórmula:    C = 5 . ( F - 32 )
                   9
                   
- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: Fahrenheit = 32   Saída: Celsius = 0.0
Teste 2: Entrada: Fahrenheit = 60   Saída: Celsius = 15.555555555555557
Teste 3: Entrada: Fahrenheit = 55   Saída: Celsius = 12.77777777777779

Fim do Comentário de várias linhas.         """

# Recebe a temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em ºF: "))
# Efetua o cálculo

celsius = 5 / 9 * (fahrenheit - 32)  # Solução 1 (parênteses obrigatórios)
# celsius = 5 * (fahrenheit - 32) / 9  # Solução 2

print("Graus em Celsius convertido", celsius)  # Mostra o resultado

''' --- ALTERAÇÕES:
a. Mostre o valor celsius com três casas decimais.
b. Altere o leiaute da mensagem de saída:
Valor em Fahrenheit: x.xx  (Mostrar com duas casas decimais).
Valor em Celsius: x.xxxx   (Mostrar com quatro casas decimais).  

'''
