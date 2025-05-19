ano = int(input(" Digite um ano de nascimento " ))
idade = 2025 - ano
if idade < 10:
    print("a pessoa é uma criança")
elif idade >= 11 and idade == 17:
    print("a pessoa é um adolescente")
elif idade >= 18 and idade <= 59:
    print(" a pessoa é um adulto")
elif idade >= 60:
    print(" a pessoa é um idoso")