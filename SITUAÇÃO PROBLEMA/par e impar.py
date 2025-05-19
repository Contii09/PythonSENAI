import random

while True:
    nome = input(" Digite seu nome ")
    print("Bom dia", nome , ",vamos jogar um jogo de par ou impar ")
    
    print("1 - impar")
    print("2 - par")
    print("3 - sair")
    escolha = int(input("Escolha: 1, 2 ou 3: "))

     
    if escolha == 3:
        break
    
    num = int(input("Digite um numero de 1 a 10: "))
    aleatorio = random.randint(1,10)
    
    print("A maquina escolheu" , aleatorio )
    
    resultado = aleatorio + num
    print("O reseultado é" , resultado)
        
    
    if resultado % 2 == 0:
        if escolha == 1:
            print("VOCE PERDEU")
        else:
            print("VOCE GANHOU")
        
    else:
        print("")
        if escolha == 2:
            print("VOCE PERDEU")
        else:
            print("VOCE GANHOU")
            