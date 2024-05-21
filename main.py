# Estamos obrigando quem for usar a função a passar os argumentos por posicao 
# Tudo que tá antes do / é obrigatório passar apenas por posicao (não aceita saldo=saldo, dá erro)
def depositar(saldo, extrato, /): 
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
    return saldo

# Aqui estamos obrigando quem for usar a funcao a passar todos os parametros pelo nome. 
# Tudo que vier depois do * tem que ser nomeado. Ex: quant_saques=3, quant_limite_saque=4....
def sacar(*, quant_saques, quant_limite_saque, saldo, extrato, valor_limite_saque):
    if(quant_saques < quant_limite_saque):
        valor = 0.0
        try:
            valor = float(input('Digite o valor a ser sacado:'))
        except:
            print('Digite um valor válido!')
        if valor > 0 and valor <= valor_limite_saque:
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
    return saldo, quant_saques

# O que tá antes do / tem que ser atributo de posicao e o que tá depois do * tem que ser nomeado
# Forma correta de passar: imprimir_extrato(10, extrato=extrato)
def imprimir_extrato(saldo, /, *, extrato):
    print('\n=========== Extrato ============\n')
    if(len(extrato) == 0):
        print('Não há movimentações na conta.')
    for transacao in extrato:
        if transacao['tipo'] == "deposito":
            print(f"+R$ {transacao["valor"]:.2f}")
        elif transacao['tipo'] == "saque":
            print(f"-R$ {transacao["valor"]:.2f}")
    print(f'\nSaldo final: {saldo:.2f}')    
    print('\n===============================\n')
    
def cadastrar_conta_corrente(cpfs_em_uso, lista_contas, prox_numero_conta):
    cpf = input('Digite o CPF do cliente (apenas números. ex: 12345678910):')
    
    # Vamos verificar se esse cpf já está em uso
    if cpf not in cpfs_em_uso:
        print('Cliente não cadastrado! Cadastre o cliente primeiro.')
        #Encerramos a execucao
        return            
    
    agencia = '0001'
    numero_conta = prox_numero_conta

    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'cpf_cliente': cpf
    }
    lista_contas.append(conta)
    print(f'Ag: {agencia} - Conta: {numero_conta} - Cliente: {cpf}: Conta cadastrada com sucesso!')
    
def cadastrar_cliente(lista_clientes, cpfs_em_uso):
    print('Vamos cadastrar um novo cliente!')
    cpf = input('Digite o CPF do cliente (apenas números. ex: 12345678910):')
    
    # Vamos verificar se esse cpf já está em uso
    if cpf in cpfs_em_uso:
        print('CPF já cadastrado!')
        #Encerramos a execucao
        return            

    nome = input('Digite o nome do cliente:')
    data_nascimento = input('Digite a data de nascimento do cliente:')
    logradouro = input('Digite o logradouro do cliente:')
    numero = input('Digite o número:')
    bairro = input('Digite o bairro:')
    cidade = input('Digite a cidade:')
    estado = input('Digite a sigla do estado em 2 letras (ex: Digite PE para Pernambuco):')

    endereco = f'{logradouro}, {numero} - {bairro} - {cidade}/{estado}'
    
    cliente = {
        'cpf': cpf,
        'nome': nome,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    }
    cpfs_em_uso.add(cpf)    
    lista_clientes.append(cliente)
    print(f'Cliente nome {nome}, cpf {cpf}, data de nascimento {data_nascimento}, endereço {endereco} cadastrado com sucesso!')

def listar_clientes(lista_clientes):
    print('\n=========== Lista de Clientes ============\n')
    if(len(lista_clientes) == 0):
        print('Não há clientes cadastrados.')
    for cliente in lista_clientes:
        print(f'Cliente: nome {cliente['nome']}, cpf {cliente['cpf']}, data de nascimento {cliente['data_nascimento']}, endereço {cliente['endereco']}')
    print('\n===============================\n')

def listar_contas(lista_contas):
    print('\n=========== Lista de Contas ============\n')
    if(len(lista_contas) == 0):
        print('Não há contas cadastradas.')
    for conta in lista_contas:
       print(f'Conta: Ag {conta['agencia']} - Conta {conta['numero_conta']} - Cliente {conta['cpf_cliente']}')
    print('\n===============================\n')
    
lista_clientes = []
lista_contas = []
cpfs_em_uso = set() #vamos criar um conjunto para consultar de forma mais rapida se o cpf já está em uso
prox_numero_conta = 0
saldo = 0.0
extrato = []
QUANT_LIMITE_SAQUE = 3
VALOR_LIMITE_SAQUE = 500
quant_saques = 0

while True:
    opcao = input('Digite uma opção: \n1-Depósito\n2-Saque\n3-Extrato\n4-Cadastrar cliente\n5-Cadastrar conta\n6-Listar clientes\n7-Listar contas\n0-Sair:')
    if opcao == '1':
        #deposito
        saldo = depositar(saldo, extrato)
    elif opcao == '2':
        #saque
        saldo, quant_saques = sacar(quant_saques=quant_saques, quant_limite_saque=QUANT_LIMITE_SAQUE, saldo=saldo, extrato=extrato, valor_limite_saque=VALOR_LIMITE_SAQUE)
        
    elif opcao == '3':
        #extrato
        imprimir_extrato(saldo, extrato=extrato)

    elif opcao == '4':
        cadastrar_cliente(lista_clientes=lista_clientes, cpfs_em_uso=cpfs_em_uso)

    elif opcao == '5':
        cadastrar_conta_corrente(cpfs_em_uso=cpfs_em_uso, lista_contas=lista_contas, prox_numero_conta=prox_numero_conta+1)

    elif opcao == '6':
        listar_clientes(lista_clientes)

    elif opcao == '7':
        listar_contas(lista_contas)

    elif opcao == '0':
        print('Obrigado por utilizar nosso sistema!')
        break

    else:
        print('Digite uma opção válida')