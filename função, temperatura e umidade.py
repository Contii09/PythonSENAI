#funçao que vefifica a temperatura
#inverno = 20 - 22
#verao = 23 - 26
#funcao que verifica a umidade
#inverno = 40 - 55
#verao = 40 - 65

num1 = int(input("Digite a temperatura "))
num2 = int(input("Digite a umidade "))
estacao = input("Em qual estação estamos, verão ou inverno? ")


def verificar_temperatura_umidade(num1,num2):
    
    if estacao == "inverno":
        if num1 >= 20 and num1 <= 22:
            print("A temperatura esta ideal")
            if num2 >= 40 and num2 <= 55:
                print("A umidade esta ideal")
            else:
                print("A umidade não está ideal")
        else:
            print("A temperatura não está ideal")
    
    
    
    elif estacao == "verao":
        if num1 >= 23 and num1 <= 26:
            print("A temperatura está ideal")
            if num2 >= 56 and num2 <= 65:
                print("A umidade está ideal")
            else:
                print("A umidade não está ideal")
        else:
            print("A temperatura não está ideal")
            
            
verificar_temperatura_umidade(num1,num2)