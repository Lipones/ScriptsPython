# -*- coding: utf-8 -*-
var1 = "Felipe"
var2 = "Silva"
seq = "ABDFRGTOHPDRTMHFJSAREAPONVOPEGRPEDVOMSOPKFSF"

tamanho = len(seq)
print (tamanho)
print(var1[0])#o numero em colchetes localiza um caractere dentro de uma sequencia de caracteres
print(var1[1])
print(seq[1:6])#podemos determinar onde iniciar e onde parar o comando
print(seq[:6])
print(seq[6:])

concatenar = (var1 + " " + var2 + "n")
print(concatenar)
print(concatenar.lower())#diminui a caixa
print(concatenar.upper())#aumenta a caixa
print(concatenar.strip("n"))#comando strip remove caracteres de uma sequencia string
print(seq.strip("A"))

minha_string = "Tês quilos de trigo para três tigres tristes"
minha_lista = minha_string.split()#comando split converte uma string em uma minha_lista
print(minha_lista)
minha_lista = minha_string.split("t")#podemos dividir as lista a partir de uma letra, letras maiusculas são case sensitive
print(minha_lista)

busca = minha_string.find("três")#comando find faz uma busca dentro da string
print(busca)
print(minha_string[busca:])#podemos utilizar a variável do comando find para exibir comente os resultados após a localização

minha_string = minha_string.replace("tristes","felizes")
print(minha_string)