from abc import ABC, abstractmethod
from datetime import date

# ------------------- Transações -------------------

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)


# ------------------- Histórico -------------------

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


# ------------------- Contas -------------------

class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True
        print("Saque não realizado. Saldo insuficiente ou valor inválido.")
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        print("Depósito inválido.")
        return False


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques diários atingido.")
            return False
        if valor > self.limite:
            print("Valor do saque excede o limite por operação.")
            return False
        if super().sacar(valor):
            self.saques_realizados += 1
            return True
        return False


# ------------------- Clientes -------------------

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
