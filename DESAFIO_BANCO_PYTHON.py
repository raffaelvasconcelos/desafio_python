menu = """\n
     Olá, bem vindo ao banco X, escolha a sua opção: 

    [D] - Depositar
    [S] - Sacar
    [E] - Extrato
    [Q] - Sair
"""


saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    print(menu)
    opcao = input('Escolha uma opção: ')
    
    if opcao == 'D':
        valor = float(input('Insira o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: {valor:.2f}\n'
            print(f'\nDepósito realizado com sucesso. Seu novo saldo é de R${saldo:.2f} reais.')
        
        else:
            print("Operação falou.")

    elif opcao == 'S':
        valor = float(input('Insira o valor de saque: '))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        execedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Saldo insuficiente.')
            

        elif excedeu_limite:
            print('Limite diário excedido.')
            

        elif execedeu_saques:
            print('Limite de saque diário excedido.')
            

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque no valor de R${valor:.2f} reais\n'
            numero_saque += 1

        else:
            print('Operação falou. Número informado inválido.')

    elif opcao == 'E':
        print("\n##########EXTRATO##########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("################################")
        

    elif opcao == 'Q':
        break

    else:
        print("\nOperação inválida.")