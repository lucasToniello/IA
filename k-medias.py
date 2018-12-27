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



def k_medias(listaClusters):

	clustersMudaram = True

	#enquanto algum clusters ainda tiverem mudanças
	while clustersMudaram:
		objetos = []

		# Atualiza os centroides dos clusters e coloca todos os objetos dos clusters em uma lista de objetos
		for cl in listaClusters:
			cl.calculaCentroide()
			
			while cl.objetos:
				objetos.append(cl.objetos.pop())

		# Para cada objeto
		for obj in objetos:

			# Acha o centroide mais próximo a ele
			obj.centroideMaisProximo(listaClusters)

			# Adiciona ele ao cluster mais próximo
 
			# Se o novo cluster for diferente do antigo, houve uma mudança
			clustersMudaram = False

		# Deleta os clusters antigos

####################################################################
############################	MAIN	############################
####################################################################

obj1 = Objeto([1, 2, 3])
obj2 = Objeto([4, 5, 6])
obj3 = Objeto([7, 8, 9])
obj4 = Objeto([10, 13, 15])
obj5 = Objeto([12, 14, 16])
obj6 = Objeto([17, 18, 19])

cl = Cluster(3)
cl.adicionaObjeto(obj1)
cl.adicionaObjeto(obj2)
cl.adicionaObjeto(obj3)

cl2 = Cluster(3)
cl2.adicionaObjeto(obj4)
cl2.adicionaObjeto(obj5)
cl2.adicionaObjeto(obj6)

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