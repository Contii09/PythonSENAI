#criar uma lista com 5 objetos
objetos = ["Lapis","Caderno","Estojo","Borracha","Caneta"]
print("Lista de objetos criadas")

#adicione um objeto 
objetos.append("Régua")
print("Objeto adicionado na lista")

#acesse o objeto que esta na segunda posição
print(objetos[1])
print("Objeto acessado na segunda posição")

#remova um objeto da lista
atualizada = objetos.pop(0)
print(atualizada)
print("Objeto removido da lista")

#exiba o tamanho da lista
print(len(objetos))
print("O tamanho da lista foi exibida")

#mostre todos os itens com for
for objeto in objetos:
    print(objeto)
    print("Os itens foram exibidos com o for")

#verifique se cadeira esta na lista.Se sim remova-a senão adicione    
if "Cadeira" in objetos:
    objetos.remove("Cadeira")
    print("A cadeira foi adicionada na lista")
    
else:
    objetos.append("Cadeira")
    print("A cadeira foi removida")

#ordene a lista em ordem alfabética   
print(objetos)
objetos.sort()
print(objetos)
print("A lista foi colocada em ordem alfabética")

#exiba o primeiro e o ultimo objeto 
ele_mento1 = len(objetos)
ele_mento2 = objetos[0]
ele_mento3 = objetos[ele_mento1 - 1]
print("Primeiro: ",ele_mento2, "Segundo: ",ele_mento3)
print("O primeiro e o ultimo numero foram exibidos")

#limpe toda a lista
objetos.clear()
print("A lista foi exibida")