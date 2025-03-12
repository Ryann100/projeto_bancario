#Menu incical contendo opções de Deposito, Saque, Extrato e Saida do sitema.

menu="""

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

#Nessa Segunda parte temos aramzenados o valor de saldo da conta, o valor limite que pode ser realizado a cada solicitação de saque, extrato, número de saques realizados_
#_como um histórico, e o limite de saques que podem ser feitos.

saldo = 2000
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

#O operador (while True:) para mater o (opcao = imput(menu)) e exibir junto no menu essa mensagem de opção.
#if serve para verificar as possiveis opcoes, posso usar if, elif ou else para isso.
#Foi usado if para verificar se a opção escolhida foi [1] se for vai retornar para colocar o valor desejado, o outro if abaixo é se a opção for [1] para deposito_
#_vai pedir para informar o valor e ele precisa ser > que 0, sendo > que 0 ele vai somar com o valor de saldo (saldo += valor do deposito) 
#Se o deposito for < que 0 o else vai apresentar uma mensagem de falha na operação, essa mensagem será executada com: print("a mensagem desejada")


#Opção [1] = Depositar


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado:"))

        if valor > 0: 
            saldo += valor
            extrato += f"Déposito realizado no valor de: R$ {valor:.2f}\n"
        else:
            print("Operação inválida!, Favor inserir um valor para deposito!.") 

#elif vai verificar um saque, o se o valor de saque excedeu o valor de saldo, se execedeu o limite a cada saque, e se execedeu o limite de numero de saques.
#Efetuando o saque já vai para o extrato informando quanto saiu da conta (quanto diminuiu do saldo) e já vai contabilizar a quantidade de saques realizados.    
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Saldo suficiente.")

        elif excedeu_limite:
            print("Operação inválida! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação inválida! Número máximo de saques realizados.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
 
        else:
            print("Operação inválida! O valor informado é inválido.")

#elif para verificar o extrato, se foi realizado saques, depositos e mostra o valor total do saldo. 
#O (\n) serve para quebra de linha.   
   
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

#elif para mostrar a mensagem de "Operação Inválida" caso nenhuma das opções 1, 2 ou 3 sejam selecionadas, para informar ao usuário que seja selecionado a operação correta.
    
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")











