#include <stdio.h>
#include <math.h>

/*Algoritmo para cálculo numérico
  especificamente INTEGRAÇÃO NUMÉRICA pela regra de SIMPSON 1/3*/

/*------------------FÓRMULA------------------*/
/*- [ h/3 * (f(x0) + 4*f(impares) + 2*f(pares) + f(xn)) ] -*/
/*--------------[ h=(b-a)/n ]--------------*/


/* definir a função da integral: */
double f(double x){
	return sin(x*x)+x;
}

/*Program begins*/
int main(){
	int n, i; /* n = numero de partes (obrigatoriamente par) */
	double a, b; /* limites inferiores e superiores */
	double h; /* tamanho do passo */
	double x; /* funcao a ser integrada (ponto no eixo x) */
	double soma_par = 0, soma_impar = 0; /* somatorios do metodo */
	double integral; /* valor resultado da integral */
	
	/* adicionar os valores para as variaveis */
	printf("\nNumero de partes n (deve ser um numero PAR): ");
	scanf("%d",&n);
	printf("\nAdicione o valor do limite inferior da integral: ");
	scanf("%lf",&a);
	printf("\nAdicione o valor do limite superior da integral: ");
	scanf("%lf",&b);
	
	/* calculando h */
	h = (b-a)/n;
	
	/* laço de repetição para o cálculo */
	for(i=1; i<n; i++){
		x = a + i*h;
		
		/* verifica se o indice e par ou impar para aplicar o peso certo */
		if(i % 2 == 0){
			soma_par = soma_par + f(x);
		} else {
			soma_impar = soma_impar + f(x);
		}
	}
	
	/* cálculo final para o valor do resultado da integral */
	integral = (h/3.0) * (f(a) + f(b) + 4*soma_impar + 2*soma_par);
	
	/* imprime o valor */
	printf("\nThe integral is: %lf\n", integral);
	
	return 0;
}
