from datetime import date
from operacao_POO import PessoaFisica, ContaCorrente, Deposito, Saque

usuarios = []
contas = []
AGENCIA = "0001"
numero_conta = 1

def cadastrar_usuario():
    cpf = input("Informe o CPF (somente números): ")

    usuario = next((u for u in usuarios if u.cpf == cpf), None)
    if usuario:
        print("Já existe usuário com esse CPF.")
        return

    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento (dd-mm-aaaa): ")
    dia, mes, ano = map(int, data_nasc.split("-"))
    endereco = input("Endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    novo_usuario = PessoaFisica(nome, cpf, date(ano, mes, dia), endereco)
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")


def criar_conta():
    global numero_conta
    cpf = input("Informe o CPF do cliente: ")

    usuario = next((u for u in usuarios if u.cpf == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Cadastre-o primeiro.")
        return

    conta = ContaCorrente.nova_conta(usuario, numero_conta)
    usuario.adicionar_conta(conta)
    contas.append(conta)
    numero_conta += 1
    print("Conta criada com sucesso!")


def depositar():
    cpf = input("Informe o CPF do cliente: ")
    usuario = next((u for u in usuarios if u.cpf == cpf), None)

    if not usuario or not usuario.contas:
        print("Usuário não encontrado ou sem conta cadastrada.")
        return

    conta = usuario.contas[0] 
    valor = float(input("Valor do depósito: R$ "))
    transacao = Deposito(valor)
    usuario.realizar_transacao(conta, transacao)


def sacar():
    cpf = input("Informe o CPF do cliente: ")
    usuario = next((u for u in usuarios if u.cpf == cpf), None)

    if not usuario or not usuario.contas:
        print("Usuário não encontrado ou sem conta cadastrada.")
        return

    conta = usuario.contas[0]
    valor = float(input("Valor do saque: R$ "))
    transacao = Saque(valor)
    usuario.realizar_transacao(conta, transacao)


def extrato():
    cpf = input("Informe o CPF do cliente: ")
    usuario = next((u for u in usuarios if u.cpf == cpf), None)

    if not usuario or not usuario.contas:
        print("Usuário não encontrado ou sem conta cadastrada.")
        return

    conta = usuario.contas[0]

    print("\n=== Extrato ===")
    if not conta.historico.transacoes:
        print("Nenhuma movimentação registrada.")
    else:
        for t in conta.historico.transacoes:
            print(f"{t.__class__.__name__}: R$ {t.valor:.2f}")

    print(f"Saldo atual: R$ {conta.saldo_atual():.2f}")
    print("===============")

menu = """
----------------------------------
(1) Cadastrar usuário
(2) Criar conta
(3) Depositar
(4) Sacar
(5) Extrato
(6) Sair
----------------------------------
"""

while True:
    opcao = input(menu)

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        criar_conta()
    elif opcao == "3":
        depositar()
    elif opcao == "4":
        sacar()
    elif opcao == "5":
        extrato()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")