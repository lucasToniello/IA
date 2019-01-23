import math

class Objeto:

	def __init__(self, nome, clusterOrigem):
		self.nome = nome
		self.clusterOrigem = clusterOrigem

def combinacaoLinear(n, p):

	if n > 1: 
		return int((math.factorial(n)) / (math.factorial(p)*math.factorial(n-p)))

	else:
		return 0

def achaObjetoCorrespondente(obj, listaResultados):

	for lResultados in listaResultados:
		if obj.nome == lResultados.nome:
			return lResultados.clusterOrigem

	# Só chega nessa parte caso o objeto não esteja na lista dos resultados
	return 0

def adjustedRandIndex(listaReais, listaResultados, numClusters):
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
	
	for i in matrizConfusao:
		for j in i:
			print(j, end=" ")
		print("\n")

	return ARI

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

numClusters = (int)(input())

F = open("average-link/saidas/saida_monkey.clu", "r")
F2 = open("datasets/monkeyReal1.clu", "r")

listaReais = leArquivo(F)
listaResultados = leArquivo(F2)

print(adjustedRandIndex(listaReais, listaResultados, numClusters))

F.close()
F2.close()