def i_m_c (peso,altura):
    return peso / ( altura * altura)

def imc_2(numero):
    if numero < 18.5:
        print("magreza" )
    elif numero >= 18.5 and numero <= 24.9:
        print("normal")
    elif numero  >= 25 and numero <= 29.9:
        print("sobrepeso")
    elif numero >= 30 and numero  <= 34.9:
        print("obesidade grau 1")
    elif numero >= 35 and numero <= 39.9:
        print("obesidade grau 2" )
    elif numero  > 40:
        print("obesidade grau 3")
 
 
peso = int(input("Digite seu peso "))
altura = float(input("Digite sua altura "))

print("O seu imc sera de: " , i_m_c(peso,altura))
numero = i_m_c(peso,altura)
imc_2(numero)