qp = 5
produtos = []
valores = []
compras = []
valor_compras = []
op = 1
cont = 0
vf = 0
desc = 0
frete = 0


qp = int(input("Quantos produtos deseja cadastrar? Digite 0 para encerrar o programa."))
if qp == 0:
    print("\nPrograma encerrado!")
else:

    for i in range(qp):
        produto = input("Insira o nome do produto:")
        produtos.append(produto)
        valor = float(input("Insira o valor do produto:"))
        valores.append(valor)
        
    print("\n======PRODUTOS CADASTRADOS======")

    for p, v in zip(produtos, valores):
        cont += 1
        print("Produto:",cont,"-",p)
        print("Valor R$:",v,"\n")

    print("\n======INÍCIO DAS COMPRAS======\n")
    print("Digite os números dos produtos que deseja comprar ou 0 para finalizar:")

    while op != 0:
        op = int(input("Digite o código do produto:"))
        if op == 0:
            print("\Compras encerradas!")
        else:
            print("Produto",op,"comprado com sucesso!\n")
            pc = produtos[op-1]
            compras.append(pc)
            vt = valores[op-1]
            valor_compras.append(vt)
            
    print("\nProdutos comprados")
            
    for c in compras:
        print(c)
        
    if sum(valor_compras) > 200:
        vf = sum(valor_compras) - sum(valor_compras)*0.10
        desc = 10
    elif sum(valor_compras) < 50:
        vf = sum(valor_compras) + 10
        frete = 10
    else:
        vf = sum(valor_compras)

    print(f"\nValor total bruto: {sum(valor_compras):.2f}")
    print("\nDesconto aplicado:",desc,"%")
    print("Valor do frete R$",frete)
    print(f"\nValor final: {vf:.2f}")
    
    print("Obrigado por comprar conosco!")



        



        
    
                 


