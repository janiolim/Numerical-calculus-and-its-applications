#include <stdio.h>
#include <math.h>

/*Algoritmo para cálculo numérico
  especificamente SISTEMAS LINEARES por ELIMINAÇÃO DE GAUSS*/

/*-----------------------FÓRMULA-----------------------*/
/*----------[ m = A[i][k] / A[k][k] ]------------------*/
/*--[ A[i][j] = A[i][j] - m * A[k][j] ]----------------*/

/*Program begins*/
int main(){
	int n, i, j, k; /* n = ordem do sistema */
	double A[20][20]; /* matriz dos coeficientes */
	double b[20]; /* vetor de termos independentes */
	double x[20]; /* vetor solucao */
	double m, soma;
	
	/* adicionar os valores para as variaveis */
	printf("\nOrdem do sistema linear (n): ");
	scanf("%d", &n);
	
	printf("\nDigite os coeficientes da matriz A:\n");
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			printf("A[%d][%d] = ", i, j);
			scanf("%lf", &A[i][j]);
		}
	}
	
	printf("\nDigite os termos independentes do vetor b:\n");
	for(i=0; i<n; i++){
		printf("b[%d] = ", i);
		scanf("%lf", &b[i]);
	}
	
	/* passo 1: eliminacao progressiva (triangularizacao da matriz) */
	for(k=0; k<n-1; k++){
		for(i=k+1; i<n; i++){
			m = A[i][k] / A[k][k]; /* calcula o multiplicador */
			
			/* zera o elemento abaixo do pivo e atualiza o resto da linha */
			for(j=k; j<n; j++){
				A[i][j] = A[i][j] - (m * A[k][j]);
			}
			/* atualiza o vetor b na mesma proporcao */
			b[i] = b[i] - (m * b[k]);
		}
	}
	
	/* passo 2: substituicao regressiva (resolvendo de tras pra frente) */
	x[n-1] = b[n-1] / A[n-1][n-1];
	
	for(i=n-2; i>=0; i--){
		soma = 0;
		for(j=i+1; j<n; j++){
			soma = soma + (A[i][j] * x[j]);
		}
		x[i] = (b[i] - soma) / A[i][i];
	}
	
	/* imprime o valor */
	printf("\nVetor solucao do sistema:\n");
	for(i=0; i<n; i++){
		printf("x[%d] = %lf\n", i, x[i]);
	}
	
	return 0;
}
