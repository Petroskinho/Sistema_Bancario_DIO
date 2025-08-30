from funcao_operacoes import *

menu = """
----------------------------------
    (1) SACAR
    (2) DEPOSITAR
    (3) EXTRATO
    (4) CADASTRAR USUÁRIO
    (5) CRIAR CONTA
    (6) SAIR
----------------------------------
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

usuarios = []   
contas = []     
AGENCIA = "0001"
numero_conta = 1

while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, limite, extrato, numero_saques = sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES_DIARIOS)

    elif opcao == "2":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "3":
        mostrar_extrato(saldo, extrato)

    elif opcao == "4":
        usuarios = cadastrar_usuario(usuarios)

    elif opcao == "5":
        contas = criar_conta(AGENCIA, numero_conta, usuarios, contas)
        numero_conta += 1  
    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        time.sleep(2)