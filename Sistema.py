class Conta:
    def __init__(self, nome, data_de_nascimento, CPF, saldo, endereco):
        self.nome = str(nome)
        self.data_de_nascimento = data_de_nascimento
        self.CPF = CPF
        self.saldo = float(saldo)
        self.endereco = str(endereco)
        self.extrato = ""
        self.numero_saques = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor, limite=500, limite_saques=3):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > limite
        excedeu_saques = self.numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("=========================================")

    def __repr__(self):
        return (f"Conta(Nome: {self.nome}, Data de Nascimento: {self.data_de_nascimento}, "
                f"CPF: {self.CPF}, Saldo: {self.saldo:.2f}, Endereço: {self.endereco})")


# Dicionário para armazenar contas
contas = {}

# Mensagem inicial
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

# Loop do menu principal
while True:
    opcao = input(Inicializar).lower()
    if opcao == "c":
        nome = input("Informe um nome para a Conta: ")
        data_de_nascimento = input("Informe a data de nascimento: ")
        CPF = input("Informe o CPF: ")
        saldo = float(input("Informe o saldo inicial: "))
        endereco = input("Informe o endereço: ")

        # Criação da nova conta
        nova_conta = Conta(nome, data_de_nascimento, CPF, saldo, endereco)
        contas[CPF] = nova_conta
        print("Conta criada com sucesso!")
        print(nova_conta)

    elif opcao == "l":
        CPF = input("Informe o CPF para logar: ")
        if CPF in contas:
            print("Logado com sucesso!")
            menu_conta(contas[CPF])
        else:
            print("Conta não encontrada.")

    elif opcao == "q":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, por favor digite novamente.")
