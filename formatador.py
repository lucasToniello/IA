####################################################################
############################	MAIN	############################
####################################################################

import sys

cluster = 0
string = " "
objetos = []
valores = []

nomeArquivo = sys.argv[1]
print("Coloque a ordem dos clusters: ")
cluster = input("Próximo cluster: ")

# Entradas: nome do arquivo de saída(gerado pelo algoritmo), mais o nome onde será salvo o arquivo .clu
F = open(nomeArquivo + ".ods", "r")
Fsaida = open(nomeArquivo + ".clu", "w")

F.readline()
string = F.readline()

while string != "":
	valores = string.split("\t");

	# Quando acha quebra de linha significa que mudamos de cluster
	if valores[0] == "\n":
		cluster = input("Próximo cluster: ")

	else:
		Fsaida.write("{}\t{}\n" .format(valores[0], cluster))

	string = F.readline()