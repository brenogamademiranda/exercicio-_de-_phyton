def mostrar_mensagem(mensagem, numero):
    print("Mensagem:", mensagem)
    print("Número:", numero)

def main():
    mensagem = input("Digite uma mensagem: ")
    numero = int(input("Digite um número: "))
    mostrar_mensagem(mensagem, numero)

main()
