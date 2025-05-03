"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.
vbc-shqr-wxd (Meet)

- Problema:
- Elabore o programa que verifica se o usuário digitou a senha correta.
Mostre a mensagem “Senha incorreta.” ou “Acesso liberado.”.
Supondo que a senha correta seja 123.

- Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Testes (se ...)
Saída de dados (escreva)

Teste 1: senha = 123            Resposta: Acesso liberado.

Teste 2: senha = 111            Resposta: Senha incorreta.
"""
senha_correta = 123             # Armazena a senha correta na memória
senha_usuario = int(input("Senha: "))
if senha_usuario == senha_correta:  # Se a senha está correta
    print("Acesso liberado.")
else:                           # Caso contrário
    print("Senha incorreta.")

''' ----- ALTERAÇÕES:
a. Considere que a senha correta é o código (string) 1b3, ou seja,
a senha correta não o número 123

'''
