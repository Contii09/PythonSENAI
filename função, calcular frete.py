#funçao que calcule o valor do frete da seguinte forma:
#valor = (peso x 0.5) + (distancia x 0.1) + taxa fixa

peso = int(input("Digite um peso "))
distancia = int(input("Digite uma distancia "))
taxa_fixa = 5

def calcular_frete(peso,distancia):
    multiplicacao1 = peso * 0.5
    multiplicacao2 = distancia * 0.1
    soma = multiplicacao1 + multiplicacao2
    valor = soma + taxa_fixa
    print("O valor será de " , valor , "reais")
    
calcular_frete(peso,distancia)
    
