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

	# calcula a distância euclidiana do objeto até outro objeto
	def distanciaEuclidiana(self, objeto):
		soma = 0
		
		for i in range (0, len(self.coordenadas)):
			soma += math.pow((objeto.coordenadas[i] - self.coordenadas[i]), 2)

		return math.sqrt(soma)

class Cluster:

	def __init__(self, objetos, numCoordenadas):
		self.objetos = objetos
		self.numCoordenadas = numCoordenadas

	def adicionaObjeto(self, objeto):
		self.objetos.append(objeto)

	def adicionaCluster(self, cluster):
		for cl in cluster.objetos:
			self.objetos.append(cl)

	def apaga(self):
		self.objetos.clear()

def single_link(objetos, k_min, k_max):

	numClusters = len(objetos)
	distancias = []

	for i in range(0, numClusters):
		objClusters.append({"status" : True, "origem" : i})

		for j in range(i+1, numClusters):
			distancias.append((i, j, objetos[i].distanciaEuclidiana(objetos[j])))

	return lista

####################################################################
############################	MAIN	############################
####################################################################

nomeArquivo = input("Nome do arquivo de entrada: ")
nomeArquivoSaida = input("Nome do arquivo de saída: ")
k_min = int(input("Número do kmin: "))
k_max = int(input("Número do kmax: "))
objetos = []

F = open(nomeArquivo, "r")
F.readline()
string = F.readline()

# Lê um arquivo de entrada contendo o nome do objeto e suas coordenadas
while string != "":
	valores = string.split("\t");
	objetos.append(Objeto(str((valores[0])), [float(valores[1]), float(valores[2])]))
	string = F.readline()

F.close()

listaClusters = single_link(objetos, k_min, k_max)
listaClusters = single_link(objetos, k_min, k_max)

plot("graficos", nomeArquivoSaida, listaClusters)
salvar("saidas", nomeArquivoSaida, listaClusters)