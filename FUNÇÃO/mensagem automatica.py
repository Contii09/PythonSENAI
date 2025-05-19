from datetime import datetime
nome = input(" Digite um nome ")

def mostra_saudacao(nome):
    hora_atual = datetime.now().hour
    

    if hora_atual = 0 and < 4:
        print("Boa madrugada" , nome)
    elif hora_atual = 5 and < 11:
        print("Bom Dia " , nome)
    elif hora_atual = 12 and  < 18:
        print("Boa tarde" , nome)
    elif hora_atual = 19 and < 23:
        print("Boa Noite" , nome)

mostra_saudacao(nome)



