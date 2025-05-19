import inputs
nomes = []

while True:
    print("Menu:")
    print("1 Cadastrar nomes dos participantes")
    print("2 Exibir o total de inscritos")
    print("3 Exibir a lista de nomes em ordem alfabéticah")
    print("4 Consultar um nome")
    print("5 Sair")
    
    opcao = inputs.input_int("Escolha uma opção: ")
    
    if opcao == 1:
        nome = inputs.input_str("Digite o nome do participante: ")
        if nome in nomes:
            print("Este nome já está na lista.")
            nomes.append(nome)
        else:
            nomes.append(nome)
            print(f"{nome} foi adicionado à lista.")

    elif opcao == 2:
        total = len(nomes)
        print(f"Total de inscritos: {total}")

    elif opcao == 3:
        nomes.sort()
        print("Lista de participantes em ordem alfabética:")
        for nome in nomes: 
            print(nome)

    elif opcao == 4:
        nome = inputs.input_str("Digite o nome que deseja consultar: ")
        if nome in nomes:
            resposta = inputs.input_str("Nome encontrado! Deseja removê-lo? (s/n): ")
            if resposta == 's':
                nomes.remove(nome)
                print(f"{nome} foi removido da lista.")
            else:
                print(f"{nome} permanece na lista.")
        else:
            resposta = inputs.input_str("Nome não encontrado. Deseja adicioná-lo? (s/n): ")
            if resposta == 's':
                nomes.append(nome)
                print(f"{nome} foi adicionado à lista.")

    elif opcao == 5:
        print("Saindo do sistema")
        break

    else:
        print("Opção inválida! Tente novamente.")