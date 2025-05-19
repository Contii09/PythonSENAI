grana  = 0
quant = 0

while True:
    print("escolha uma opção")
    print("")
    print("[1] Adicionar o valor da despesa")
    print("[2] mostrar quantidade e valor total das despesas")
    print("[0] sair")
    num = input("escolha uma das opções ")


    if num == "1":
        gasto = int(input("valor gasto"))
        print(gasto, "reais")
        grana = grana + gasto
        quant += 1
    elif num == "2":
        print(grana ,'reais')
        print("quantidade de despesas=",quant)
    elif num == "0":
        print("sair")
        break 

