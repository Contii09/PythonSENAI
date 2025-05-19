nota1 = int(input("digite um numero "))
nota2 = int(input("digite um numero "))

media1 = nota1 + nota2
mediafinal = media1 / 2

if mediafinal >= 70:
    aluno = "aprovado"
   
elif mediafinal < 70:
    aluno = "reprovado"
   
print("o aluno esta", aluno ,)