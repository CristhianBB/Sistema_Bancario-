from datetime import date

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao:
    def registrar(self, conta):
        raise NotImplementedError

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(f"Depósito: R$ {self.valor:.2f}")
        print("Depósito realizado com sucesso!")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > conta.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif self.valor > conta.limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif conta.numero_saques >= conta.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque: R$ {self.valor:.2f}")
            conta.numero_saques += 1
            print("Saque realizado com sucesso!")

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

    def sacar(self, valor):
        saque = Saque(valor)
        saque.registrar(self)

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.historico.transacoes:
                print(transacao)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("=========================================")

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite, limite_saques):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
      
contas = {}


Inicializar = """
Bem Vindo senhor(a), por favor digitar:
[l] para Logar na Conta 
[c] para Criar uma Conta
[q] para sair 
"""

def menu_conta(conta):
    menu_do_usuario = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    while True:
        opcao = input(menu_do_usuario).lower()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)
        elif opcao == "e":
            conta.exibir_extrato()
        elif opcao == "q":
            print("Saindo do menu da conta...")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


while True:
    opcao = input(Inicializar).lower()
    if opcao == "c":
        nome = input("Informe um nome para a Conta: ")
        data_de_nascimento = input("Informe a data de nascimento (YYYY-MM-DD): ")
        cpf = input("Informe o CPF: ")
        endereco = input("Informe o endereço: ")
        agencia = input("Informe a agência: ")
        numero = int(input("Informe o número da conta: "))
        limite = float(input("Informe o limite de saque: "))
        limite_saques = int(input("Informe o limite de saques por dia: "))

        cliente = PessoaFisica(cpf, nome, date.fromisoformat(data_de_nascimento), endereco)
        nova_conta = ContaCorrente(numero, agencia, cliente, limite, limite_saques)
        cliente.adicionar_conta(nova_conta)
        contas[cpf] = nova_conta
        print("Conta criada com sucesso!")
        print(nova_conta)

    elif opcao == "l":
        cpf = input("Informe o CPF para logar: ")
        if cpf in contas:
            print("Logado com sucesso!")
            menu_conta(contas[cpf])
        else:
            print("Conta não encontrada.")

    elif opcao == "q":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, por favor digite novamente.")
