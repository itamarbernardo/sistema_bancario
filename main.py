saldo = 0.0
extrato = []
QUANT_LIMITE_SAQUE = 3
VALOR_LIMITE_SAQUE = 500
quant_saques = 0

while True:
    opcao = input('Digite uma opção: \n1-Depósito\n2-Saque\n3-Extrato\n0-Sair:')
    if opcao == '1':
        #deposito
        valor = 0.0
        try:
            valor = float(input('Digite o valor a ser depositado:'))
        except:
            print('Digite um valor válido!')    
        if valor > 0:
            saldo += valor
            print('Depósito realizado com sucesso!')
            extrato.append({"tipo": "deposito", "valor": valor})
        else:
            print('Digite um valor positivo')
    elif opcao == '2':
        #saque
        if(quant_saques < QUANT_LIMITE_SAQUE):
            valor = 0.0
            try:
                valor = float(input('Digite o valor a ser sacado:'))
            except:
                print('Digite um valor válido!')
            if valor > 0 and valor <= VALOR_LIMITE_SAQUE:
                if valor <= saldo:
                    saldo -= valor
                    print('Saque realizado com sucesso!')
                    quant_saques+=1
                    extrato.append({"tipo": "saque", "valor": valor})
                else:
                    print(f'Seu saldo de {saldo} é insuficiente para sacar {valor}')
            else:
                if valor <= 0:
                    print('Digite um valor maior que zero a ser sacado')
                else:
                    print('O limite de saque é até R$ 500 por saque')
        else:
            print('Limite de 3 saques por dia atingido. Tente novamente amanhã')
        
    elif opcao == '3':
        #extrato
        print('\n=========== Extrato ============\n')
        if(len(extrato) == 0):
            print('Não há movimentações na conta.')
        for transacao in extrato:
            tipo = transacao["tipo"]
            if transacao['tipo'] == "deposito":
                print(f"+R$ {transacao["valor"]:.2f}")
            elif transacao['tipo'] == "saque":
                print(f"-R$ {transacao["valor"]:.2f}")
        print(f'\nSaldo final: {saldo:.2f}')    
        print('\n===============================\n')
    elif opcao == '0':
        print('Obrigado por utilizar nosso sistema!')
        break
    else:
        print('Digite uma opção válida')