"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

Crie um novo programa dentro do mesmo projeto:
- Coluna esquerda - mouse direito no nome do projeto (PythonProject)
  New - Python File
- Digite o nome do programa Python sem espaço e sem acentuação - <Enter>

- Problema:
- Implemente o programa que calcule a média aritmética de duas notas
bimestrais fornecidas pelo usuário.

- Fórmula:  média = nota1 + nota2
                          2

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: nota1: 4.5 e nota2: 6.1             Saída: 5.3
Teste 2: Entrada: nota1: 7.5 e nota2: 5.1             Saída: 6.3

Fim do Comentário de várias linhas.             """

nota1 = float(input("Primeira nota: "))  # Converte os valores para float
nota2 = float(input("Segunda nota: "))

# Atribui o cálculo à variável media
media = (nota1 + nota2) / 2             # Parênteses obrigatórios.

print("Média:", media)                  # Mostra o resultado

''' --- ALTERAÇÕES:
a. Mostre a média com duas casas decimais
b. Acrescente, considere que o aluno realizou três avaliações. 
   Teste 3: Entrada: nota1: 2, nota2: 3 e nota3: 4       Saída: 3
c. Na execução, pule três linhas antes de mostrar o valor da média. 
d. Depois da média, mostre também o valor das três notas.
e. Acrescente o cálculo da média ponderada, considerando que a nota1 
   tem peso 1, a nota2 tem peso 2 e a nota3 tem peso 3.  
   Teste com os valores 5, 6, 7.       A resposta certa é 6,3333333
f. Agora, refaça-o sem usar a variável media.     

'''
