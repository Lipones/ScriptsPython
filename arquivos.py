# -*- coding: utf-8 -*-
#Arquivos

#função open

#variavel = open (nome, modo)

# r = somente leitura
# w = escrita (caso o arquivo exista ele será apagado e um novo arquivo vazio será criado)
# a = leitura e escrita (adiciona o novo conteudo ao fim do arquivo)
# r+ = leitura e escrita
# w+ = escrita ( o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
# a+ = leitura e escrita (abre o arquivo para atualização)#

#read() lê o arquivo inteiro
#readline() lê uma linha
#readlines() lê o arquivo e armazena em uma lista

arquivo = open("hello word.txt")
print(arquivo)
linhas = arquivo.readlines()
print(linhas)
for linhas in linhas:
	print(linhas)
texto_completo = arquivo.read()
print(texto_completo)

w = open("arquivo2.txt", "a")# esse comando cria o arquivo, cuidado com a extensão
w.write("esse é o meu arquivo\n")#esse comando escreve dados no arquivo
w.close()#comando usado para fechar arquivo, útil quando estamos abrindo e gravando vários arquivos