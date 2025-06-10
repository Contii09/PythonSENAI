#funcao que receba uma distancia em km e uma velocidade
#Calcule quanto tempo levara para fazer o percurso

distancia = int(input("Digite uma distancia em km "))
velocidade = int(input("Digite uma velociade "))

def calcular_tempo(distancia,velocidade):
    tempo = distancia / velocidade
    print("O tempo sera de " , tempo)
    
calcular_tempo(distancia,velocidade)
    