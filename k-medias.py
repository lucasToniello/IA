####################################################################
###################    Algoritmo k-médias	########################
####################################################################
import math

class Objeto:

	# Parâmetros: lista de coordenadas
	def __init__(self, coordenadas):

		# self.nome = nome
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
		return novoCentroide


def k_medias(listaClusters):

	objetos = []
	centroides = [0, 0] # Tem que mudar isso obviamente
	clustersMudaram = True
	indice = 0
	i = 0

	for cl in listaClusters:
		centroides[i] = cl.calculaCentroide()
			
		while cl.objetos:
			objetos.append(cl.objetos.pop())

		i = i+1

	#enquanto algum cluster ainda tiver sofrido mudança
	while clustersMudaram:

		# Para cada objeto
		for obj in objetos:

			# Acha o centroide mais próximo a ele
			indice = obj.centroideMaisProximo(listaClusters)

			# Adiciona ele ao cluster mais próximo
			listaClusters[indice].objetos.append(obj)

			# Eliminar centroides sem objetos...? talvez tirar eles do cálculo na distância euclidiana?

		objetos = []
		clustersMudaram = False
		i = 0

		for cl in listaClusters:
			temp = cl.calculaCentroide()

			if temp != centroides[i]:
				clustersMudaram = True

			centroides[i] = temp
		
			if clustersMudaram:
				while cl.objetos:
					objetos.append(cl.objetos.pop())

			i = i+1

		for cl in listaClusters:
			print("Novo cluster: ")
				for obj in cl.objetos:
					print(obj.coordenadas)

####################################################################
############################	MAIN	############################
####################################################################

objA = Objeto([1.5, 6])
objB = Objeto([2, 5])
objC = Objeto([2.5, 4])
objD = Objeto([3, 3.5])
objE = Objeto([3, 2])
objF = Objeto([2.5, 2])

cl = Cluster(2)
cl.adicionaObjeto(objA)
cl.adicionaObjeto(objB)

cl2 = Cluster(2)
cl.adicionaObjeto(objC)
cl2.adicionaObjeto(objD)
cl2.adicionaObjeto(objE)
cl2.adicionaObjeto(objF)

# cl.calculaCentroide()
# print(cl.centroide)

# cl2.calculaCentroide()
# print(cl2.centroide)

# cl.adicionaObjeto(obj4)
# cl.adicionaObjeto(obj5)
# cl.adicionaObjeto(obj6)
# cl.calculaCentroide()
# print(cl.centroide)

listaClusters = []
listaClusters.append(cl)
listaClusters.append(cl2)

k_medias(listaClusters)