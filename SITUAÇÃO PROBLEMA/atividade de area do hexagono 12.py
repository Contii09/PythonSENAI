# obter os numeros
#1 calcular a area do triangulo
# descobrir quanto é lado vezes lado
# descobrir a raiz de 3
#2 calcular a area do hexagono
# multiplicar a area do triangulo vezes 6
# exibir a area do triangulo e do hexagono

lado = int(input("Digite um valor para o lado do triangulo"))
lado2 = lado * lado
raiz =  round(3 ** 0.5 , 2)
lado3 = lado2 * raiz
area_triangulo = lado3 / 4
print(" A área do triangulo é" , area_triangulo)

area_hexagono = area_triangulo * 6
print(" A área do hexagono é" , area_hexagono)