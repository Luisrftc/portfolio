cont = 1
senha = 0
op = 0
dep = 0
saq = 0
saldo = 1000

#Senha de acesso

senha = int(input("Informe sua senha:"))
print("Senha inválida!")

if senha!=1234:
    while cont<=2:
        senha = int(input("Informe sua senha:"))
        cont+=1
        if cont < 3:
            print("Senha inválida!")
        else:
            print("Senha bloqueada!")
else:
            
#Início do menu

    print("MENU CAIXA ELETRÔNICO\n")
    print("1-Consultar saldo\n")
    print("2-Realizar depósito\n")
    print("3-Efetuar saque\n")
    print("4-Sair\n")

    while op != 4:

        op = int(input("Informe a opção desejada:"))
        
        if op == 1:
            print(f"O seu saldo é de R$ {saldo:.2f}")
            
        elif op == 2:
            dep = float(input("Informe o valor do depósito:"))
            if dep == 0:
                print("O valor do depósito deve ser maior que zero")
            else:
                saldo = saldo + dep
        
        elif op == 3:
            saq = float(input("Informe o valor do saque:"))
            if saq == 0:
                print("O valor do saque deve ser maior que zero!")
            elif saq > saldo:
                print("Saldo insuficiente para saque!")
            else:
                saldo = saldo - saq
            
        elif op == 4:
            print("Sessão encerrada! Obrigado!")
        
        else:
            print("Opção inválida! Tente novamente!")
    
    
    
        

    


