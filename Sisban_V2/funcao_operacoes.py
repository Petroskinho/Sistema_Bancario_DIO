import time

def sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES_DIARIOS):
    if numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("Você já atingiu o limite de saques diários!")
        time.sleep(2)
        return saldo, limite, extrato, numero_saques

    saque = float(input("Quanto você gostaria de sacar? R$ "))
    time.sleep(2)

    if saque > limite or saque > saldo:
        print(f"Esse saque ultrapassa seu limite diário ou saldo. "
              f"Seu limite diário de saque é de R$ {limite:.2f} e seu saldo atual é R$ {saldo:.2f}")
        time.sleep(2)

    elif saque <= 0:
        print("Valor inválido! O saque deve ser maior que zero.")
        time.sleep(2)

    else:
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        time.sleep(2)
        extrato += f"Foi realizado um saque de R$ {saque:.2f}.\n"
        limite -= saque
        saldo -= saque
        numero_saques += 1

    return saldo, limite, extrato, numero_saques


def depositar(saldo, extrato):
    deposito = float(input("Quanto você gostaria de depositar? R$ "))
    saldo += deposito
    extrato += f"Foi realizado um depósito de R$ {deposito:.2f}\n"

    print(f"\nDepósito de R$ {deposito:.2f} realizado! Agora seu saldo é de R$ {saldo:.2f}.")
    time.sleep(2)

    return saldo, extrato


def mostrar_extrato(saldo, extrato):
    if extrato == "":
        print("Não foram realizadas transações")
    else:
        print(extrato)
        print(f"\nSeu saldo atual é de R$ {saldo:.2f}")
    time.sleep(2)


# ------------------ Funções de Usuário e Conta ------------------

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario_existente = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario_existente:
        print("Já existe um usuário com esse CPF!")
        time.sleep(2)
        return usuarios

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")
    time.sleep(2)
    return usuarios


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")

    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario:
        contas.append({
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print("Conta criada com sucesso!")
        time.sleep(2)
    else:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        time.sleep(2)

    return contas