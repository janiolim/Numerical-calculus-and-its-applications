#include <stdio.h>

/*Algoritmo para cálculo numérico
  especificamente INTERPOLAÇÃO pelo POLINÔMIO DE LAGRANGE*/

/*-----------------------FÓRMULA-----------------------*/
/*---------[ P(x) = somatorio( y_i * L_i(x) ) ]--------*/
/*---[ L_i(x) = produtorio( (x - x_j)/(x_i - x_j) )]---*/

/*Program begins*/
int main(){
	int n, i, j; /* n = numero de pontos */
	double x_int; /* ponto x que queremos descobrir o y */
	double x[100], y[100]; /* vetores para armazenar os pontos tabelados */
	double L, P = 0; /* L = termo de Lagrange, P = valor final interpolado */
	
	/* adicionar os valores para as variaveis */
	printf("\nNumero de pontos tabelados: ");
	scanf("%d", &n);
	
	printf("\nDigite as coordenadas dos pontos (x e y):\n");
	for(i=0; i<n; i++){
		printf("x[%d] = ", i);
		scanf("%lf", &x[i]);
		printf("y[%d] = ", i);
		scanf("%lf", &y[i]);
	}
	
	printf("\nDigite o valor de x para interpolar: ");
	scanf("%lf", &x_int);
	
	/* laço de repetição para o cálculo */
	for(i=0; i<n; i++){
		L = 1; /* o produtorio sempre comeca em 1 */
		
		for(j=0; j<n; j++){
			if(j != i){
				L = L * ((x_int - x[j]) / (x[i] - x[j]));
			}
		}
		
		/* somatorio do polinomio */
		P = P + (y[i] * L);
	}
	
	/* imprime o valor */
	printf("\nO valor interpolado e: %lf\n", P);
	
	return 0;
}
