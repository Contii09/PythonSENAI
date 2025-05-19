import random
aleatorio = random.randint(1,100)
nome = input("Digite seu nome ")
print("Bom Dia" , nome , ",vamos jogar um jogo de adivinhação")


while True:
    num = int(input("Digite um número de 0 a 100: "))
   
    if num == aleatorio:
        print("VOCE GANHOU")
        print("deseja jogar novamente:")
        print("1 - sim")
        print("2 - não")
        escolha = int(input("escolha uma opção "))
        if escolha == 1:
            aleatorio = random.randint(1,100)
            continue
        elif escolha == 2:
            break 
    
    elif aleatorio > num:
            print("O numero é maior que", num)
            
    elif aleatorio < num:
            print("O numero é menor que" , num)
            
         
        
        
            