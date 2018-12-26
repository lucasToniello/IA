####################################################################
###################  Algoritmo single-link	########################
####################################################################
						
import math

#calcula a distância euclidiana dados duas tuplas de coordenadas (carai eu usei a palavra tupla em uma matéria que não é do zé)
def distanciaEuclidiana(x1, x2):

	soma = 0

	#se as tuplas tiverem tamanhos diferentes, não é possível fazer o cálculo
	if len(x1) != len(x2):
		return -1

	for i in range (0, len(x1)):
		soma += math.pow((x2[i] - x1[i]), 2)

	return math.sqrt(soma)

#def calculaMatriz(objetos):

	# while len(objetos):
		# print('\n{} -> ' .format(objetos[0][0]), end="")

		# for i in range(1, len(objetos)):
			# print('{:.2f} ({})' .format(distanciaEuclidiana(objetos[0][1], objetos[i][1]), objetos[i][0]), end="  ")

		# objetos.pop(0)

####################################################################
############################	MAIN	############################
####################################################################

obj1 = [2.5, 3.5]
obj2 = [6, 1]

print(distanciaEuclidiana(obj1, obj2))