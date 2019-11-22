
#####################################################################
###################  Algoritmo average-link	########################
####################################################################

import math
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(1, '../')

from util import plot, salvar

class Objeto:

    def __init__ (self, nome, coordenadas):
        self.nome = nome
        self.coordenadas = coordenadas

    def distanciaEuclidiana(self,objeto):
        soma = 0

        for i in range (0, len(self.coordenadas)):
            soma += math.pow((objeto.coordenadas[i] - self.coordenadas[i]), 2)
        
        soma = math.sqrt(soma)
        soma /= (len(objeto.coordenadas) * len(self.coordenadas))

        return soma

def buscarMenor(list):
    menor = (2**32) - 1
    objMenor = []
    for key in list:
        if key[2] < menor:
            menor = key[2]
            x = key[0]
            y = key[1]
                    
    objMenor.append((x,y,menor))
    return objMenor
     

def calcularAverage(ObjA,ObjB):
    soma = 0
    listaClusters = []
    # calcular a distancia do novo cluster
    for i in range (0,len(ObjA)):
        soma = (ObjA[i][2] + ObjB[i][2])/2
        listaClusters.append((ObjA[i][0], ObjA[i][1],soma))
    return listaClusters 

def average_link(objetos,k_min,k_max):

    numClusters = len(objetos)
    distancias = []
    listaClusters = []

    for i in range(0, numClusters):
        for j in range(i+1, numClusters):
            distancias.append((i, j, objetos[i].distanciaEuclidiana(objetos[j])))

    while numClusters > k_min:
        
        
        pegarMenor = buscarMenor(distancias)

        #excluir o menor da distancia
        for i in range(0, len(distancias)):
            if distancias[i][0] == pegarMenor[0][0] and distancias[i][1] == pegarMenor[0][1]:
                d = distancias.pop(i)
                break  
        min_index = d[0]
        max_index = d[1]
        #pegar todas as distancias ndo ObjA e ObjB
        ObjA = []
        ObjB = []

        for i in range(0, len(distancias)):
            if distancias[i][1] == min_index or distancias[i][0] == min_index:
                pos_i = distancias[i][0] 
                pos_j = distancias[i][1]
                ObjA.append((pos_i,pos_j,distancias[i][2]))
            
            if distancias[i][1] == max_index or distancias[i][0] == max_index:
                pos_i = distancias[i][0] 
                pos_j = distancias[i][1]
                ObjB.append((pos_i,pos_j,distancias[i][2]))
        
        listaClusters = calcularAverage(ObjA,ObjB)

        for i in range (0,len(ObjA)):
            distancias.remove(ObjA[i])
            distancias.remove(ObjB[i])
        fim = time.time()
       
        distancias.extend(listaClusters) 
        listaClusters.clear()

        numClusters = numClusters - 1
    
    return distancias

####################################################################
############################	MAIN	############################
####################################################################

nomeArquivo = sys.argv[1]
nomeArquivoSaida = sys.argv[2]
k_min = int(sys.argv[3])
k_max = int(sys.argv[4])
listaClusters = []
objetos = []

F = open(nomeArquivo, "r")
F.readline()
string = F.readline()

while string != "":
    valores = string.split("\t");
    objetos.append(Objeto(str((valores[0])), [float(valores[1]), float(valores[2])]))
    string = F.readline()

F.close()

listaClusters = average_link(objetos,k_min,k_max)

plot("graficos", nomeArquivoSaida, listaClusters)
salvar("saidas", nomeArquivoSaida, listaClusters)