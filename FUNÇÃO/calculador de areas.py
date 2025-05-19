def area_circulo(raio):
    pi = 3.14
    return pi * raio * raio
def area_quadrado(lado1,lado2):
    return lado1 * lado2
def area_retangulo(lado1,lado2):
    return lado1 * lado2
def area_triangulo(lado1):
    return lado1 * lado1 * 0.5 / 4
def area_hexagono():
    return area_triangulo(lado1) * 6


def perimetro_circulo():
    return 2 * pi * raio
def perimetro_quadrado():
    return lado1 + lado1 + lado2 + lado2
def perimetro_retangulo():
    return lado1 + lado1 + lado2 + lado2
def perimetro_triangulo():
    return lado1 + lado1 + lado2
def perimetro_hexagono():
    return  lado1 + lado1 + lado1 + lado2 + lado2 + lado2


def menu_area_e_perimetro():
    print("escolha uma opçao ")
    print("1 - area_circulo")
    print("2 - area_quadrado")
    print("3 - area_retangulo")
    print("4 - area_triangulo")
    print("5 - area_hexagono")
    print("6 - perimetro_circulo")
    print("7 - perimetro_quadrado")
    print("8 - perimetro_retangulo")
    print("9 - perimetro_triangulo")
    print("10 - perimetro_hexagono")

    escolha = int(input("escolha um numero "))
    if escolha == 1:
        raio = int(input("Digite um numero para o raio "))
        print("A area do circulo é", area_circulo(raio))
       
    elif escolha == 2:
        lado1 = int(input("Digite um numero para o lado "))
        lado2 = int(input("Digite outro numero para outro lado "))
        print("A area do do quadrado é", area_quadrado(lado1,lado2))
       
    elif escolha == 3:
        lado1 = int(input("Digite um numero para o lado "))
        lado2 = int(input("Digite outro numero para outro lado "))
        print("A area do retangulo ", area_retangulo(lado1,lado2))
       
    elif escolha == 4:
        lado1 = int(input("Digite um numero para o lado "))
        print("A area do triangulo é ", area_triangulo(lado1))
       
    elif escolha == 5:
        print("A area do hexagono é ", area_hexagono())
       
    elif escolha == 6:
        print("O perimetro do circulo é ", perimetro_circulo())
       
    elif escolha == 7:
        print("O perimetro do quadrado é ", perimetro_quadrado())
       
    elif escolha == 8:
        print("O perimetro do retangulo é ", perimetro_retangulo())
       
    elif escolha == 9:
        print("O perimetro do triangulo é ", perimetro_triangulo())
       
    elif escolha == 10:
        print("O perimetro do hexagono é ", perimetro_hexagono())
   

menu_area_e_perimetro()