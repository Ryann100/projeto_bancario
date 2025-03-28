#Projeto Bancário, update do primeiro projeto alterando e acrescentando mais funcionalidades.

import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome =nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class PessoaJuridica(cliente):
    def __init__(self, nome, data_nascimento, cnpj, data_abertura, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cnpj = cnpj
        self.data_abertura = data_abertura
        
class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif valor > 0:
            self.saldo -= valor
            print("\n Saque realizado com sucesso! ")
            return True
        
        else:
            print("\n Erro! Valor inválido. ")
            return False
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("\n Deposito realizado com sucesso! ")

        else:
            print("\n Erro! Valor inválido. ")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=1000, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transação for transação in self]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite: 
            print("\n Erro! O valor de saque excede o limite. ")

        elif excedeu_saques:
            print("\n Erro! Número máximo de saques realizados. ")

        else:
            return super().sacar(valor)

        return False

    def __str__ (self):
        return f"""\
            Agência: \t{self.agencia}
            C/C: \t\t{self.numero}
            Titular: \t{self.cliente.nome}
        """     
    
class ContaBlack(Conta):

    def __init__(self, numero, clinte):
        super().__init__(numero, cliente)

        def sacar(self, valor):
            [transação for transação in self]

            return super().sacar(valor)
        
        return False

class historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"), 
            }
        )    

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self.valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

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

def filtrar_usuario(cpf, clientes):
    clientes_filtrados = [clientes for cliente in clientes if clientes.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None 

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n Cliente não possui conta ")
        return

    #FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_usuario(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado! ")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("n\ Cliente não possui uma conta! ")
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_usuario(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado! ")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("n\ Cliente não possui uma conta! ")
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(cliente):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_usuario(cpf, cliente)

    if not cliente:
        print("n\ Cliente não encontrado! ")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_cliente_PF(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_usuario(cpf, clientes)

    if cliente:
        print("\n CPF já cadastrado! ")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n Usuário criado com sucesso! ")

def criar_cliente_PJ(clientes):
    cnpj = input("Informe o CNPJ (somente números):")
    cliente = filtrar_usuario(cnpj, clientes)

    if cliente:
        print("\n CNPJ já cadastrado! ")
        return

    nome = input("Informe o nome da empresa: ")
    data_nascimento = input("Informe a data de fundação (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado)")

    cliente = PessoaJuridica(nome=nome, data_nascimento=data_nascimento, cnpj=cnpj, endereco=endereco)

    clientes.append(cliente)

    print("\n Conta criado com sucesso! ")

def criar_conta(numero_conta, clientes, contas):
    cpf_cnpj = input("Informe o CPF do cliente ou CNPJ (somente números): ")
    cliente = filtrar_usuario(cpf_cnpj, clientes)

    if cliente:
        print("\n Documento vinculado a uma conta existente! ")
        return
    
    tipo_cliente = input("Tipe de cliente (1-PF/2-PJ): ").strip()

    if tipo_cliente == "1": #Pessoa Fisica
        nome = input("Informe o nome completo:")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endreco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")
        
        cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf_cnpj, endereco=endereco)
        
    elif tipo_cliente == "2": #Pessoa Juridica
        razao_social = input("Informe a razão social: ")
        nome_fantasia = input("Informe o nome fantasia: ")
        data_fundacao = input("Informe a data de fundação (dd-mm-aaaa): ")
        endereco = input("Informe o endereço comercial: ")
        cliente = PessoaJuridica(razao_social=razao_social, nome_fantasia=nome_fantasia, cnpj=cpf_cnpj, data_fundacao=data_fundacao, endereco=endereco)

    else:
        print("\n Tipo de cliente inválido! ")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    clientes.append(cliente)
    print("\n Cliente criado com sucesso! ")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:
        opcao =menu ()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_cliente_PF(clientes)

        elif opcao == "5":
            criar_cliente_PJ(clientes)
            
        elif opcao == "6":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "7":
            listar_contas(contas)

        elif opcao == "8":
            break

        else:
            print("\n Operação inválida, por favor selecione novamente a operação desejada. ")

main()
