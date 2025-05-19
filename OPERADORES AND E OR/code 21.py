l1 = int(input("Digite um número "))
l2 = int(input("Digite um número "))
l3 = int(input("Digite um número "))

if l1 != l2 and l1 != l3 and l2 != l3:
    print("triangulo escaleno")

if l1 == l2 and l1 != l3 and l2 != l3 or l1 == l3 and l1 != l2 and l3 != l2 or l3 == l2 and l3 != l1 and l2 != l1:
    print("triangulo isosceles")
if l1 == l2 == l3:
    print("triangulo equilatero")


