import inputs
def soma(num1, num2):
    return num1 + num2
def subtração(num1, num2):
    return num1 - num2
def multiplicação(num1, num2):
    return num1 * num2
def divisão(num1, num2):
    return num1 / num2

def exibir(num1, num2):
    print("soma ", soma(num1, num2))
    print("subtração", subtração(num1, num2))
    print("multiplicação", multiplicação(num1, num2))
    print("divisão ", divisão(num1, num2))


def menu_calculadora():
    print("escolha uma opção ")
    print("1 - soma ")
    print("2 - subtração ")
    print("3 - multiplicação ")
    print("4 - divisão ")
    print("5 - todas as opções ")

    while True:
        try:
            opção = inputs.input_int("escolha uma opção: ")
            if opção >= 1 and opção <= 5:
                break
            else:
                print("número invalido ")
        except ValueError:
            print("digite outro número ")
       
    while True:
        try:
            num1 = inputs.input_int("digite um número ")
            break
        except ValueError:
            print("digite somente números ")
               
    while True:
        try:
            num2 = inputs.input_int("digite outro número ")
            break
        except ValueError:
            print("digite somente números ")
                   
    if opção == 1:
        print("soma ", soma(num1, num2))
                           
    elif opção == 2:
        print("subtração ", subtração(num1, num2))
                           
    elif opção == 3:
        print("multiplicação ", multiplicação(num1, num2))
                           
    elif opção == 4:
        print("divisão ", divisão(num1, num2))
                         
    elif opção == 5:
        exibir(num1, num2)
                                   
           
while True:
    menu_calculadora()