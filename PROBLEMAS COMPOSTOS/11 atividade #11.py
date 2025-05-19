#1 quantos litros e qual valor que serao necessarios para completar a viagem
# qual a distancia da viagem
# quantos km ja foram percorridos
# qual a autonomia do carro por litro
# quantos litros ha no tanque
# qual o preço do combustivel

#2 passo a passo
#subtarir a distancia por quanto foi percorrido
# dividir a distancia pela autonomia
# subtrair o combustivel pelo litro
# multiplicar o valor pelo preço
# exibir o valor gasto em reais e o quanto de combustivel sera necessario




viagem = 800
autonomia = 7
tanque = 10
distancia = 90
preço = 6.90
km =  int(viagem - distancia)
litro1 = int(km / autonomia)
litro2 = int(litro1 - tanque)
valor1 = int(litro2 * preço)


print("o valor do combustivel é de:" , valor1 , "reais")
print("serao necessarios " , litro2 , "litros")
