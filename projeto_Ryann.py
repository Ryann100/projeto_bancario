#Menu incical (Botões de funcionalidades).
import textwrap

def menu():
    menu ="""\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCriar Conta
    [5]\tCriar Usuário
    [6]\tListar Contas
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))

#Função de Deposito (Usando if para retornar valor e somar ao saldo e extrato. Else para gerar erro caso insira valor zero ou negativo).

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Valor De Déposito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("@@@ Erro na opreação! Favor inserir um valor para deposito!. @@@")

    return saldo, extrato

#Função de Saque (Usado para validar váriaves de saque, limite, saldo...).

def sacar(* , saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("@@@ Operação falhou! Saldo insuficiente. @@@")

    elif excedeu_limite:
        print("@@@ Operação falhou! Saldo execede o limite de saque. @@@")
        
    elif excedeu_saques:
        print("@@@ Operação falhou! Número máximo de saques atingido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 2
        print("\n=== Saque realizado com sucesso! Aguarde a saida do dinheiro. ===")
    else:
        print("@@@ Operação falhou! O valor inserido é inválido. @@@")

    return saldo, extrato

#Função de Extrato (Usado para detalhar as transações de cada usuário).

def exibir_extrato(saldo, / , *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)    
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

#Função de criação de Usuário (É obrigátorio Nome, CPF, Data De Nascimento, Endereço).

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ CPF já cadastrado! @@@")
        return
    
    nome = input("Insira o nome completo:")
    data_nascimento = input("Insira sua data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

#Filtrar Usuário (Filtro para saber se existe já o usuário conforme as informações preenchidas).

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o número de CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
        print("\n@@@ Usuário não cadastrado, favor criar usuário! @@@")

#Cria uma lista com todas as contas dos usuários.

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

#Main, responsável por validar limites, valores de saque, saldo, extrato e funções do menu.

def main():
    LIMITE_SAQUES = 5
    AGENCIA = "0001"

    saldo = 0
    limite = 100
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Insira o valor de depósito:"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Insira o valor para o saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")


main()        




    




    















