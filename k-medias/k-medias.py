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
	# obs: se a lista de centroides estiver vazia vai dar erro na linha 27 (corrigir?)
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

	# Precisa dessa função...?
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
		# print(novoCentroide)


def k_medias(objetos, numClusters, iteracoes):

	indice = 0
	listaClusters = []

	# Inicia a lista de clusters, gerando aleatóriamente seus centroides
	for i in range(0, numClusters):

		# Escolhemos aleatóriamente seu centroide (garantir que não é igual a nenhum dos outros)
		indiceCentroide = random.randint(0, len(objetos) - 1)
		listaClusters.append(Cluster(2))
		listaClusters[i].centroide = objetos[indiceCentroide].coordenadas
		print(listaClusters[i].centroide)

	while iteracoes:

		# Para cada objeto
		for obj in objetos:

			# Acha o centroide mais próximo a ele
			indice = obj.centroideMaisProximo(listaClusters)

			# Adiciona ele ao cluster mais próximo
			listaClusters[indice].adicionaObjeto(obj)

		for cl in listaClusters:
			print("Novo cluster: ")
			for obj in cl.objetos:
				print("{} - {}" .format(obj.nome, obj.coordenadas))

		iteracoes = iteracoes-1
		objetos = []

		for cl in listaClusters:
			cl.calculaCentroide()
			
			while cl.objetos:
				objetos.append(cl.objetos.pop(0))

		print("\n\n")

####################################################################
############################	MAIN	############################
####################################################################

F = open("../teste.txt", "r")
string = " "
objetos = []

F.readline()
string = F.readline()

while string != "":
	valores = string.split("\t");
	objetos.append(Objeto(valores[0], [float(valores[1]), float(valores[2])]))
	string = F.readline()

for obj in objetos:
	print("{} - {}" .format(obj.nome, obj.coordenadas))

k_medias(objetos, 2, 3)