ano = int(input(" Digite um ano de nascimento"))
idade = 2025 - ano
variavel = ""
if idade >= 18:
    variavel = "maior de idade"
else:
    variavel = " menor de idade"
print(idade, " ele é " , variavel)
    
    