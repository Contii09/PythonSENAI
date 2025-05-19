nota1 = int(input("Digite uma nota entre 0 a 100 " ))
nota2 = int(input("Digite outra nota entre 0 a 100 " ))

soma = nota1 + nota2
media = soma / 2
if nota1 > 0 and nota1 <= 100 and nota2 > 0 and nota2 <= 100:
    

    if media >= 70:
        print("o aluno está aprovado")
    elif media >= 50 and media > 70:
        print(" o aluno esta em recupereção")
    elif media < 50:
        print("o aluno esta reprovado")
else:
    print(" digite um numero de 0 a 100")
