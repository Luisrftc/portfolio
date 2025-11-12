senha = 1234
saldo = 50
produto = 30
op = 0
login = 0

while login != senha:
    login = int(input("Informe sua senha:"))
    if login == senha:
        print("Acesso liberado!")
    else:
        print("Senha inválida!")
        
        
while op != 4:
    print("\n=======MENU========")
    print("1 - Ver saldo do cliente\n")
    print("2 - Ver preço do produto\n")
    print("3 - Comprar produto\n")
    print("4 - Sair\n")
        
    op = int(input("Escolha uma opção:"))
        
    if op == 1:
        print(f"Seu saldo é de R$ {saldo:.2f}\n")
            
    elif op == 2:
        print("Fone de Ouvido - R$ 30,00")
            
    elif op == 3:
        if produto > saldo:
            print("Saldo insuficiente!")
        else:
            print("Produto comprado no valor de R$ 30,00")
            saldo = saldo - produto
            
    elif op == 4:
        print("Sessão encerrada!")
                 
    else:
        print("Opção inválida! Tente novamente!")
            
