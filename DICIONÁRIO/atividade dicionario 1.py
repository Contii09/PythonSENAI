#1
print("PRIMEIRO LIVRO")
livros_1 = {
    "nome": "Imperfeitos",
    "preço": 25,
    "genero": "romance",
    "lancamento": 2021
}

livros_1["autora"] = "Christina Lauren"

livros_1["lancamento"] = 2022

del  livros_1 ["lancamento"]

if "genero" in  livros_1:
    print("Genero está presente")
else:
    print("Genero inexistente")
    
for chave, valor in livros_1.items():
    print(f"{chave}: {valor}")
    

print(".")
print(".")
print(".")

#2
print("SEGUNDO LIVRO")
livros_2 = {
    "nome": "É assim que acaba",
    "preço": 30,
    "genero": "romance",
    "lancamento": 2015
}

livros_2["autora"] = "Colleen Hoover"

livros_2["lancamento"] = 2026

del livros_2 ["lancamento"]

if "genero" in livros_2:
    print("Genero está presente")
else:
    print("Genero inexistente")
    
for chave, valor in livros_2.items():
    print(f"{chave}: {valor}")
    


print(".")
print(".")
print(".")

#3
print("TERCEIRO LIVRO")
livros_3 = {
    "nome": "A culpa é das estrelas",
    "preço": 40,
    "genero": "romance",
    "lancamento": 2013
}

livros_3["autora"] = "John Green"

livros_3["lancamento"] = 2012

del livros_3 ["lancamento"]

if "genero" in livros_3:
    print("Genero está presente")
else:
    print("Genero inexistente")
    
for chave, valor in livros_3.items():
    print(f"{chave}: {valor}")
    
print(".")
print(".")
print(".")

print("EXIBIR TODOS OS LIVROS")
# Exibir uma lista de dicionarios
lista_livros = [livros_1,livros_2,livros_3]

    #escolhendo campos
for livros in lista_livros:
    print(f"{livros['nome']}")

print(".")
print(".")
print(".")

    # exibindo todos
for livros in lista_livros:
    for chave, valor in livros.items():
        print(f"{chave} - {valor}")
    print()
