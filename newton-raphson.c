#include <stdio.h>
#include <math.h>
/*Algoritmo para cálculo numérico
  especificamente ZEROS DE FUNÇÕES pelo método de NEWTON-RAPHSON*/

/*------------------FÓRMULA------------------*/
/*----------[ x = x0 - f(x0)/f'(x0) ]--------*/


/* definir a função: */
double f(double x){
	return (x*x*x)-x-2;
}

/* derivada da função: */
double df(double x){
	return 3*(x*x)-1;
}
 
/*Program begins*/
int main(){
	int max_it=100, i=0; /* limites de repeticao */
	double x0, x1; /* x0 = chute inicial, x1 = proximo valor */
	double tol; /* tolerancia */
	
	/* adicionar os valores para as variaveis */
	printf("\nChute inicial: ");
	scanf("%lf",&x0);
	printf("\nAdicione a tolerancia: ");
	scanf("%lf",&tol);
	
	/* laço de repetição para o cálculo */
	for(i=0; i<max_it; i++){
		x1 = x0 - (f(x0)/df(x0));
		
		/* verificacao do criterio de parada */
		if(fabs(x1 - x0) < tol){
			break;
		}
		
		/* prepara para a proxima iteracao */
		x0 = x1;
	}
	
	/* imprime o valor */
	printf("\nA raiz e: %lf\n",x1);
	printf("Iteracoes: %d\n", i+1);
}
