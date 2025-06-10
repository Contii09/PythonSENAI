#O usuário possa informar o nome do aluno. 
#O sistema receba três notas e calcule a média automaticamente. 
#Com base na média, o sistema deve indicar se o aluno está "Aprovado"import inputs (média ≥ 7), "Recuperação" (entre 5 e 6.9) ou "Reprovado" (média < 5). 
#O sistema deve permitir o cadastro de vários alunos e exibir um resumo final com o nome de cada aluno e sua situação.
import inputs
alunos = []

        
def cadastrar_alunos():
    nome = inputs.input_str("Digite o nome ")
    nota1 = inputs.input_int("Digite a primeira nota ")
    nota2 = inputs.input_int("Digite a segunda nota ")
    nota3 = inputs.input_int("Digite a terceira nota ")
    media = calcular_media(nota1,nota2,nota3)
    situacao = verificar_situacao(media)
    aluno = {
        "nomes": nome,
        "notas1": nota1,
        "notas2": nota2,
        "notas3": nota3,
        "medias": media,
        "situações": situacao
    }
    
    
    if aluno in alunos:
        print("Este aluno já está na lista.")
    else:
        alunos.append(aluno)
        print(" Seu nome foi cadastrado com sucesso!")
        
   
def calcular_media(nota1,nota2,nota3):
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media
    print("A média é" , media)



def verificar_situacao(media):
    if media >= 7:
        print("APROVADO")

    elif media >= 5 and media <= 6.9:
        print("RECUPERAÇÃO")

    elif media < 5:
        print("REPROVADO")
    


def mostrar_relatorio(alunos):
    for ordem1 in alunos:
        for chave, valor in ordem1.items():
            print(f' {chave}:  {valor}')
        print("")
    
    
    
while True:
    print("   --- MENU ---")
    print("1. Cadastrar um aluno")
    print("2. Relatorio")
    print("3. Sair")
  
    opcao = input("Escolha uma opção: ")
    
    if opcao == "3":
        print("Você chegou ao fim...")
        break
    
    if opcao == "1":
        cadastrar_alunos()
        

    elif opcao == "2":
        mostrar_relatorio(alunos)
        