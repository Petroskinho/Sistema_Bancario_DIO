import time

menu = """
----------------------------------
    (1) SACAR
    (2) DEPOSITAR
    (3) EXTRATO
    (4) SAIR
----------------------------------
"""

saldo = 0;
limite = 500;
extrato = "";
numero_saques = 0;
LIMITE_SAQUES_DIARIOS = 3;

while True:

    opcao = input(menu);
    
    if opcao == "1":
        if numero_saques >= LIMITE_SAQUES_DIARIOS:
            print("Você já atingiu o limite de saques diários!")
            time.sleep(2)
        else:
            while True:
                saque = float(input("Quanto você gostaria de sacar? R$ "))
                time.sleep(2)

                if saque > limite or saque > saldo:
                    print(f"Esse saque ultrapassa seu limite diário ou saldo. Seu limite diário de saque é de R$ {limite:.2f} e seu saldo atual é R$ {saldo:.2f}")
                    time.sleep(2)
                    break

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
                    break
                    

    elif opcao == "2":
        deposito = float(input("Quanto voce gostaria de depositar? R$ "))
        saldo += deposito

        extrato += f"Foi realizado um deposito de R$ {deposito:.2f}\n"

        print(f"\nDepósito de R$ {deposito:.2f} realizado! Agora seu saldo é de R$ {saldo:.2f}.")
        time.sleep(2)

    elif opcao == "3":
        if extrato == "":
            print("Não foram realizadas transações")
            time.sleep(2)
        else:
            print(extrato)
            time.sleep(2)
            print(f"\nSeu saldo atual é de R$ {saldo:.2f}")
            time.sleep(2)

    elif opcao == "4":
        break