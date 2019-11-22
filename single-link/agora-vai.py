import numpy as np 
import sys
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import os

def salvar(dirSaidas, nome, listaClusters):
	if not os.path.exists(dirSaidas):
		os.mkdir(dirSaidas)

	Fsaida = open(dirSaidas + "/" + nome, "w")
	
	for cl in listaClusters:
	    Fsaida.write("c2sp1s1\t{}\n" .format(cl))
        
	Fsaida.close()

# Exemplo de entrada python3 average_link.py <objetos de entrada> <nome_arquivo_saida> <k_min> <k_max> 
nomeArquivo = sys.argv[1]
nomeArquivoSaida = sys.argv[2]
k_min = int(sys.argv[3])
k_max = int(sys.argv[4])
objetos = []

#abertura do arquivo com leitura
F = open(nomeArquivo, "r")
F.readline()
string = F.readline()

while string != "":
    valores = string.split("\t");
    objetos.append((float(valores[1]),float(valores[2])))
    string = F.readline()
F.close()

X = np.array(objetos)

i = 1
for j in range(k_min, k_max + 1):
    resultimage_name = nomeArquivoSaida + "_" + str(j) + ".png"
    
    cluster = AgglomerativeClustering(n_clusters=j, affinity='euclidean', linkage='single')
    cluster.fit_predict(X)

    plt.scatter(X[:, 0], X[:, 1], c=cluster.labels_, cmap='rainbow')

    plt.title(nomeArquivoSaida + "_" + str(j))
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo y")
    #plt.legend(loc="lower left", fontsize="x-small")
    plt.savefig(resultimage_name)
    nome = nomeArquivoSaida + "_" + str(j) + ".clu"
    salvar("Resultados",nome,cluster.labels_)
    i=+1



