from empresa import cliente, tratamento_erro

map_cliente = {}
print('Opção 1 - Cliente')
print('Opção 4 - Sair')

op = tratamento_erro.erro()
while (op != 1) & (op !=4):
    op = tratamento_erro.erro()

while op != 4:
    print("")
    print('Opção 1 - Cadastrar Cliente')
    print('Opção 2 - Consultar Cliente Cadastrado')
    print('Opção 3 - Editar Cliente Cadastrado')
    print('Opção 4 - Sair')
    op = tratamento_erro.erro()

    if op == 1:
        print('Quantos clientes você quer cadastrar?')
        quant = tratamento_erro.erro()
        for x in range(1, quant + 1):
            nome = str(input('Nome: '))
            endereco = str(input('Endereço: '))
            email = str(input('E-mail: '))
            telefone = tratamento_erro.telefone_erro()
            print('')
            dados_cliente = cliente.Dados(nome, endereco, email, telefone)
            map_cliente.update({x: dados_cliente.consulta()})

    elif op == 2:
        for chave in map_cliente.keys():
            print(f'{chave} {map_cliente[chave]}')

    elif op == 3:
        print('Qual código do cliente você quer editar?')
        cod = tratamento_erro.erro()
        try:
            while cod > x:
                print('Código inválido!')
                cod = tratamento_erro.erro()
        except NameError:
            op = int(input('Não existe cliente cadastrado para ser editado! Digite a opção 1 para cadastrar.'))

        for chave in map_cliente.keys():
            if chave == cod:
                nome = str(input('Nome: '))
                endereco = str(input('Endereço: '))
                email = str(input('E-mail: '))
                telefone = tratamento_erro.telefone_erro()
                print('')
                dados_cliente = cliente.Dados(nome, endereco, email, telefone)
                dados_cliente.editar(nome, endereco, email, telefone)
                map_cliente.update({chave: dados_cliente.consulta()})

    elif op == 4:
        print('Saindo....')





