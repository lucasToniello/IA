import os
import matplotlib.pyplot as plt

def plot(dirImagens, nome, listaClusters):
	i = 1;

	if not os.path.exists(dirImagens):
		os.mkdir(dirImagens)
	
	for cl in listaClusters:
		x = []
		y = []

		cl.objetos.sort(key = lambda x: x.nome)

		for obj in cl.objetos:
			x.append(obj.coordenadas[0])
			y.append(obj.coordenadas[1])

		plt.scatter(x, y, label="Cluster " + str(i))
		i += 1

	plt.title(nome)
	plt.xlabel("Eixo x")
	plt.ylabel("Eixo y")
	plt.legend(loc="lower left", fontsize="x-small")
	plt.savefig(dirImagens + "/" + nome + ".png")


def salvar(dirSaidas, nome, listaClusters):
	if not os.path.exists(dirSaidas):
		os.mkdir(dirSaidas)

	Fsaida = open(dirSaidas + "/" + nome + ".ods", "w")
	Fsaida.write("sample label\td1\td2\n")

	for cl in listaClusters:
		cl.objetos.sort(key = lambda x: x.nome)

		for obj in cl.objetos:
			Fsaida.write("{}\t{:.8f}\t{:.8f}\n" .format(obj.nome, obj.coordenadas[0], obj.coordenadas[1]))

		Fsaida.write("\n")

	Fsaida.close()