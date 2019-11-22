####################################################################
###################    Algoritmo single-link	####################
####################################################################
import sys
import math
import random

sys.path.insert(1, '../')

from util import plot, salvar

class Objeto:

	# Parâmetros: nome, lista de coordenadas
	def __init__(self, nome, coordenadas):
		self.nome = nome
		self.coordenadas = coordenadas

	# calcula a distância euclidiana do objeto até outro objeto (obs: eles devem possuir o mesmo número de coordenadas)
	# Fazer uma exceção pra caso não tenham???
	def distanciaEuclidiana(self, objeto):
		soma = 0
		
		for i in range (0, len(self.coordenadas)):
			soma += math.pow((objeto.coordenadas[i] - self.coordenadas[i]), 2)

		return math.sqrt(soma)

class Cluster:

	def __init__(self, numCoordenadas, objetos=[]):
		self.objetos = objetos
		self.numCoordenadas = numCoordenadas

	def adicionaObjeto(self, objeto):
		self.objetos.append(objeto)

	def adicionaCluster(self, cluster):
		for cl in cluster.objetos:
			self.objetos.append(cl)

	def apaga(self):
		self.objetos.clear()

def single_link(listaClusters, k_min, k_max, nomeArquivoSaida):

	numGraficos = 0
	numClusters = len(listaClusters)

	# Enquanto o número de clusters for maior que o k_min
	while numClusters > k_min:

		menor = (2**32) - 1
		soma = 0

		# Calcula todas as distâncias e acha a menor
		for i in range(0, numClusters):
			for objA in listaClusters[i].objetos:
				
				for j in range(i+1, numClusters):
					for objB in listaClusters[j].objetos:
						
						dist = objA.distanciaEuclidiana(objB)
						soma += 1
						if dist < menor:
							menor = dist
							min_indice = i
							max_indice = j

		print(soma)

		# Agora, devemos "linkar" os clusters, passando todos os clusters de um para o outro e eliminando o que ficou sem clusters
		listaClusters[min_indice].adicionaCluster(listaClusters[max_indice])
		listaClusters.pop(max_indice)
		numClusters = numClusters - 1

		if numClusters <= k_max:
			numGraficos += 1
			plot(numGraficos, "graficos", nomeArquivoSaida + str(numClusters), listaClusters)
			salvar("saidas", nomeArquivoSaida + str(numClusters), listaClusters)

		# print(numClusters)

	return listaClusters # Tem que mudar isso pra uma lista

####################################################################
############################	MAIN	############################
####################################################################

# input("Nome do arquivo de entrada: ")
nomeArquivo = sys.argv[1]
nomeArquivoSaida = sys.argv[2]
k_min = int(sys.argv[3])
k_max = int(sys.argv[4])
listaClusters = []

F = open(nomeArquivo, "r")
F.readline()
string = F.readline()

# Lê um arquivo de entrada contendo o nome do objeto e suas coordenadas
while string != "":
	valores = string.split("\t");
	listaClusters.append(Cluster(2, [Objeto(str((valores[0])), [float(valores[1]), float(valores[2])])]))
	string = F.readline()

F.close()

listaClusters = single_link(listaClusters, k_min, k_max, nomeArquivoSaida)