
import sys
import os


def salvar(dirSaidas, nome, listaClusters):
	if not os.path.exists(dirSaidas):
		os.mkdir(dirSaidas)

	Fsaida = open(dirSaidas + "/" + nome, "w")
	
	for cl in listaClusters:
	    Fsaida.write("{}\n" .format(cl))
        
	Fsaida.close()

nomeArquivo = sys.argv[1]
nomeArquivoSaida = sys.argv[2]

objetos = []

#abertura do arquivo com leitura
F = open(nomeArquivo, "r")
F.readline()
string = F.readline()

while string != "":
    valores = string.split("\t");
    objetos.append((int(valores[1])))
    string = F.readline()
F.close()

nome = nomeArquivoSaida + ".clu"

salvar("Clu",nome,objetos)