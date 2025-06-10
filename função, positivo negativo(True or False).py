#função que verifique se o numero é positivo ou negativo e retorne True ou False

num = int(input("Digite um numero "))
def verificar(num):
       
    if num > 0:
        return True
    
    else:
        return False

verificar(num)