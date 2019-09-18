#-*_ coding utf-8 -*-

#listas numéricas
lista1 = [1,2,3,4,5,6]
#listas Strings
lista2 = ["pedra","papel","tesoura"]
#lista mista
lista3 = ["pedra", 2, 3.5, True, False]
print(lista1)
print(lista2)
print(lista3)
print(lista2[2])#imprime a posição correspondente na lista que começa por 0

for item in lista3:#utilização do laço for para imprimir a lista
	print(item)

tamanho = len(lista2)#imprimindo oa tamanho da lista
print(tamanho)

lista1.append(7)#comando append faz a inserção de um novo item na lista
print(lista1)

if 7 in lista1:
	print("o valor existe na lista")#utilizar if para verificar redundancia

del lista1[5:]#removendo itens a partir de uma posição, não colocar nada depois do : indica remoção até o final da lista
print(lista1)

lista2.sort()#comando sort ordena as listas,funciona com listas strings
print(lista2)
lista2.sort(reverse = True)#também funciona para inverter a ordem das strings
print(lista2)

del lista2[:]#deletar a lista inteira
print(lista2)

lista4 = []
lista4.append(1)#criando uma nova lista, um comando por vez
print(lista4)

lista5 = [345,123,768,45,67,78,4,5,0]
lista5.reverse()#comando para reverter a lista
print(lista5)
lista5.sort()#comando para ordenação de listas existentes
print(lista5)
lista5 = sorted(lista5)#comando sorted cria uma nova lista ordenada
print(lista5)
lista5.sort(reverse = True)#para ordenar a lista em ordem decrescente
print(lista5)









