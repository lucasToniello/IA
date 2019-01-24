####################################################################
###################    Algoritmo k-médias	########################
####################################################################
import math
import random

class Objeto:

	# Parâmetros: lista de coordenadas
	def __init__(self, nome, coordenadas):

		self.nome = nome
		self.coordenadas = coordenadas

	# calcula a distância euclidiana do objeto até um centroide -- Parâmetros: centroide
	def distanciaEuclidiana(self, centroide):
		soma = 0
		
		for i in range (0, len(centroide)):
			soma += math.pow((centroide[i] - self.coordenadas[i]), 2)

		return math.sqrt(soma)

	# retorna o índice do centróide mais próximo ao objeto -- Parâmetros: lista de clusters
	def centroideMaisProximo(self, clusters):

		menor = self.distanciaEuclidiana(clusters[0].centroide)
		indice = 0

		for i in range(1, len(clusters)):
			temp = self.distanciaEuclidiana(clusters[i].centroide)

			if temp < menor:
				menor = temp
				indice = i

		return indice

class Cluster:

	def __init__(self, numCoordenadas):
		self.objetos = []
		self.centroide = []
		self.numCoordenadas = numCoordenadas

	def adicionaObjeto(self, objeto):
		self.objetos.append(objeto)

	# Atualiza o centroide do cluster
	def calculaCentroide(self):
		it = 0
		novoCentroide = []

		while it < self.numCoordenadas:
			soma = 0

			for obj in self.objetos:
				soma += obj.coordenadas[it]

			novoCentroide.append(soma/len(self.objetos)) # Criar uma variável para o número de objetos?
			it = it + 1									 # Ai não precisa chamar a função len toda hora

		self.centroide = novoCentroide

def k_medias(objetos, numClusters, iteracoes):

	i = 0
	indice = 0
	listaClusters = []

	# Inicia a lista de clusters, gerando aleatóriamente seus centroides
	for i in range(0, numClusters):

		# Escolhemos aleatóriamente seu centroide
		indiceCentroide = random.randint(0, len(objetos) - 1)
		listaClusters.append(Cluster(2))
		listaClusters[i].centroide = objetos[indiceCentroide].numCoordenadas

	while iteracoes:

		# Para cada objeto
		for obj in objetos:

			# Acha o centroide mais próximo a ele
			indice = obj.centroideMaisProximo(listaClusters)

			# Adiciona ele ao cluster mais próximo
			listaClusters[indice].adicionaObjeto(obj)

		# Diminui o número de iterações e apaga a lista de objetos
		iteracoes = iteracoes-1
		objetos = []

		# Caso não seja a última iteração
		if iteracoes:
			
			# Para cada cluster, atualizamos seu centróide e então passamos todos seus objetos para a lista de objetos
			for cl in listaClusters:
				cl.calculaCentroide()
				
				while cl.objetos:
					objetos.append(cl.objetos.pop(0))

	return listaClusters

####################################################################
############################	MAIN	############################
####################################################################

nomeArquivo = input()
numClusters = (int)(input())
iteracoes = (int)(input())

string = " "
objetos = []
F = open(nomeArquivo, "r")

F.readline()
string = F.readline()

# Lê um arquivo de entrada contendo o nome do objeto e suas coordenadas
while string != "":
	valores = string.split("\t");
	objetos.append(Objeto(str((valores[0])), [float(valores[1]), float(valores[2])]))
	string = F.readline()

# Executa o algoritmo k-medias
listaClusters = k_medias(objetos, numClusters, iteracoes)

# E então printa sua saída de acordo com o arquivo padrão
print("sample label\td1\td2")
for cl in listaClusters:
	# Para simplificar a visualização, ordenamos os objetos do cluster por ordem alfabética
	cl.objetos.sort(key = lambda x: x.nome)

	for obj in cl.objetos:
		print("{}\t{:.8f}\t{:.8f}" .format(obj.nome, obj.coordenadas[0], obj.coordenadas[1]))

	# Quebra de linha para separar os clusters
	print("\n")

f.close()