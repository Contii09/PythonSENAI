import inputs
pais = []
presentes = []
ausentes = []
while True:
    print("Menu:")
    print("1. Cadastrar nomes dos pais")
    print("2. Exibir o total de pais")
    print("3. Exibir a lista de nomes em ordem alfabética")
    print("4. Confirmar presença dos pais")
    print("5. Exibir relatório da chamada")
    print("6. Sair")

    opcao = inputs.input_int("Escolha uma opção: ")
    
    if opcao == 1:
        nome = inputs.input_str("Digite o nome do pai ou da mãe: ")
        if nome in pais:
            print("Este nome já está na lista.")
        else:
            pais.append(nome)
            print(f"{nome} foi adicionado à lista.")

    elif opcao == 2:
        total = len(pais)
        print(f"Total de pais cadastrados: {total}")

    elif opcao == 3:
        pais.sort()
        print("Lista de pais em ordem alfabética:")
        for nome in pais:
            print(nome)

    elif opcao == 4:
        presentes = []
        ausentes = []
        
        for nome in pais:
            resposta = inputs.input_str(f"{nome} está presente? (s/n): ")
            if resposta == 's':
                presentes.append(nome)
            else:
                ausentes.append(nome)

    elif opcao == 5:
        print("Relatório da chamada:")
        print("Pais presentes:")
        for nome in presentes:
            print(nome)
        
        print("Pais ausentes:")
        for nome in ausentes:
            print(nome)

    elif opcao == 6:
        print("Saindo do sistema")
        break

    else:
        print("Opção inválida! Tente novamente")