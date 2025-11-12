senha = 1234
saldo = 10
op = 0
passagem = 0
vpas = 0
recarga = 0
login = 0

while login != senha:
    login = int(input("Informe sua senha:"))
    if login == senha:
        print("Acesso liberado!")
    else:
        print("Senha inválida!")

    
while op != 4:
    print("\n=======MENU========")
    print("1 - Consultar saldo\n")
    print("2 - Recarregar cartão\n")
    print("3 - Comprar passagem\n")
    print("4 - Sair\n")
        
    op = int(input("Escolha uma opção:"))
        
    if op == 1:
        print(f"Seu saldo é de R$ {saldo:.2f}\n")
                 
    elif op == 2:
        recarga = float(input("Informe o valor da recarga:"))
        if recarga >= 5:
            saldo = saldo + recarga
            print(f"Recarga de R$ {recarga:.2f} realizada com sucesso!\n")
        else:
            print("Valor de recarga inválido! Valor mínimo de R$ 5,00.\n")
                 
    elif op == 3:
        passagem = int(input("Informe quantas passagens deseja comprar:"))
        if saldo < 4.40 or saldo < passagem*4.40:
            print("Saldo insuficiente!\n")
        else:
            print(f"{passagem} passagem(s) compradas!\n")
            vpas = passagem*4.40
            saldo = saldo - vpas
            print(f"Valor total de R$ {vpas:.2f}")
                 
    elif op == 4:
        print("Sessão encerrada!")
                 
    else:
        print("Opção inválida! Tente novamente!")
            
