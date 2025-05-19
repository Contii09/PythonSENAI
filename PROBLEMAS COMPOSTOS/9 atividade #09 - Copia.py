# descobrir o valor que falta para completar o tanque
# subtrair a capacidade do tanque pela quantidade de litros ja colocados no tanque
#2 multiplicar o valor que falta para completar o tanque pelo preço do combustivel
#3 exibir o valor gasto para completar o tanque

nome1 = float(input("digite a capacidade do tanque "))
nome2 = float(input("digite o valor de combustivel presente no tanque "))
nome3 = float(input("digite o valor do combustivel "))
litros = nome1 - nome2
valor = litros * nome3

print("o valor gasto pra encher o tanque é " , valor)