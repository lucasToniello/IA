import os
import sys
import math

class Objeto:

	def __init__(self, nome, clusterOrigem):
		self.nome = nome
		self.clusterOrigem = clusterOrigem

# Calcula combinação linear entre n e p
def combinacaoLinear(n, p):

	if n > 1: 
		return int((math.factorial(n)) / (math.factorial(p)*math.factorial(n-p)))

	else:
		return 0

# Acha o objeto correspondente na lista de resultados
def achaObjetoCorrespondente(obj, listaResultados):

	for lResultados in listaResultados:
		if obj.nome == lResultados.nome:
			return lResultados.clusterOrigem

	# Só chega nessa parte caso o objeto não esteja na lista dos resultados
	return 0

def adjustedRandIndex(saida, listaReais, listaResultados, numClusters):
	indice = 0

	# Inicializa a matriz de confusão
	matrizConfusao = []
	for i in range(0, numClusters):
		matrizConfusao.append([0 for i in range(0, numClusters)])

	# Para cada objeto da lista das origens:
	for lreais in listaReais:

		# Procura o correspondente na lista de resultados
		indice = achaObjetoCorrespondente(lreais, listaResultados)

		# E adiciona um valor na matriz de confusão com base na comparação do cluster esperado e achado
		matrizConfusao[lreais.clusterOrigem-1][indice-1] += 1

	# Calcula o ARI com base na matriz de confusão
	somaGeral = 0
	somaLinhas = 0
	somaColunas = 0
	ARI = 0

	for i in range(0, numClusters):
		temp1 = 0
		temp2 = 0

		for j in range(0, numClusters):
			somaGeral += combinacaoLinear(matrizConfusao[i][j], 2)
			temp1 += matrizConfusao[i][j]
			temp2 += matrizConfusao[j][i]

		somaLinhas += combinacaoLinear(temp1, 2)
		somaColunas += combinacaoLinear(temp2, 2)

	ARI = somaGeral - ((somaLinhas*somaColunas) / combinacaoLinear(len(listaReais), 2))
	ARI /= (0.5*(somaLinhas+somaColunas)) - ((somaLinhas*somaColunas) / combinacaoLinear(len(listaReais), 2))
	
	if not os.path.exists("comparacoes"):
		os.mkdir("comparacoes")

	print("comparacoes/" + saida + ".ods")

	FSaida = open("comparacoes/" + saida + ".ods", "w")
	FSaida.write("Matriz de Confusão:\n")

	# Printa a matriz de confusão
	for i in matrizConfusao:
		for j in i:
			FSaida.write("{}\t" .format(j))
		FSaida.write("\n")

	FSaida.write("Índice RAND: {}" .format(ARI))
	FSaida.close()

	# E retorna o índice rand ajustado
	return ARI

# Lê um arquivo com os objetos: seu nome mais suas coordenadas
def leArquivo(F):

	string = " "
	lista = []
	string = F.readline()

	while string != "":
		valores = string.split("\t")
		lista.append(Objeto(valores[0], int(valores[1])))
		string = F.readline()

	return lista

####################################################################
############################	MAIN	############################
####################################################################

listaReais = []
listaResultados = []

# Entradas: número de clusters dos arquivos mais seus nomes
numClusters = int(sys.argv[1])
arquivoReal = sys.argv[2]
arquivoResultados = sys.argv[3]
saida = sys.argv[4]

F = open(arquivoReal, "r")
F2 = open(arquivoResultados, "r")

listaReais = leArquivo(F)
listaResultados = leArquivo(F2)

F.close()
F2.close()

print(adjustedRandIndex(saida, listaReais, listaResultados, numClusters))