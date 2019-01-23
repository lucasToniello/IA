/*####################################################################
###################  Algoritmo single-link	########################
####################################################################*/
						
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

typedef struct{
	string nome;
	double d1;
	double d2;
} objeto;

typedef struct{
	vector<objeto> objetos;
}cluster;


//calcula a distância euclidiana entre dois clusters com n objetos cada. Cada objeto com dois atributos
double distanciaEuclidiana(cluster c1, cluster c2){
	double menorDist = (double)INT32_MAX;
	for(int i = 0; i < c1.objetos.size(); i++){
		for(int j = 0; j < c2.objetos.size(); j++){
			double d = pow((c1.objetos[i].d1-c2.objetos[j].d1), 2) + pow((c2.objetos[j].d2-c1.objetos[i].d2), 2);
			if(d < menorDist)
				menorDist = d;
		}
	} 
	return sqrt(menorDist); 
}

int main(){
	vector<cluster> clusters;

	cluster c;
	objeto p;
	// recebe objetos e seus atributos
	while(cin >> p.nome){
		cin >> p.d1 >> p.d2;

		c.objetos.push_back(p);
		clusters.push_back(c);
		c.objetos.clear();
	}

	int kmin = 5, kmax = 12;
	while(clusters.size() > kmin){
		double menorDist = (double)INT32_MAX;
		int menor_i, menor_j;
		double m;

		// calcula distancias e guarda a menor entre dois objetos/clusters
		for(int i = 0; i < clusters.size(); i++){
			for(int j = 0; j < i; j++){
				m = distanciaEuclidiana(clusters[i], clusters[j]);

				if(m < menorDist){
					menorDist = m;
					menor_i = i;
					menor_j = j;
				}

				if(m == menorDist && clusters[i].objetos.size()+clusters[j].objetos.size() > clusters[menor_i].objetos.size()+clusters[menor_j].objetos.size()){
					menorDist = m;
					menor_i = i;
					menor_j = j;
				}
			}
		}

		// atualiza clusters juntando os dois com menor distancia entre eles
		for(int i = 0; i < clusters[menor_j].objetos.size(); i++){
			clusters[menor_i].objetos.push_back(clusters[menor_j].objetos[i]);
		}
		clusters.erase(clusters.begin()+menor_j);		

		// imprime o conteudo de todos os clusters
		if(clusters.size() <= kmax){
			for(int i = 0; i < clusters.size(); i++){
				for(int j = 0; j < clusters[i].objetos.size(); j++)
					cout << clusters[i].objetos[j].nome << " ";
				cout << endl; 
			}
			cout << endl;
		}
	}


	return 0;
}