def soma(num1,num2):
    return num1 + num2
def subtraçao(num1,num2):
    return num1 - num2
def divisao(num1,num2):
    return num1 / num2
def multiplicaçao(num1,num2):
    return num1 * num2

def menu_calculadora():
    print("escolha uma opçao ")
    print("1 - soma")
    print("2 - subtraçao")
    print("3 - divisao")
    print("4 - multiplicaçao")

    operacao = int(input("Escolha uma operaçao "))

    if operacao == 1:
        print(soma(num1,num2))
    elif operacao == 2:
        print(subtraçao(num1,num2))
    elif operacao == 3:
        print(divisao(num1,num2))
    elif operacao == 4:
        print(multiplicaçao(num1,num2))
    

def total_operacoes():
    print("a soma é igual a", 1)
    print("a subtraçao é igual a", 2)
    print("a divisao é igual a", 3)
    print("a multiplicaçao é igual a", 4)
       
       
num1 = int(input("digite um numero "))
num2 = int(input("digite outro numero "))

menu_calculadora()

total_operacoes()










