#include <stdio.h>
#include <math.h>
/*Algoritmo criado por Francisco Jânio para cálculo numérico
  especificamente INTEGRAÇÃO NUMÉRICA pela regra do TRAPÉZIO*/

/*------------------FÓRMULA------------------*/
/*----------[ h(f(a)/2 + f(b)/2) ]----------*/
/*--------------[ h=(b-a)/n ]--------------*/


/* definir a função da integral: */
double f(double x){
  return sin(x*x)+x;
}
 
/*Program begins*/
int main(){
	int n,i; /* n = número de partes */
	double a,b; /* limites inferiores e superiores */
	double h; /* esqueci oque h representa */
	double x; /* função a ser integrada */
	double val_int=0,integral; /* "valor_integral=0" e valor resultado da integral */
	
	/* adicionar os valores para as variaveis */
	printf("\nNúmero de partes de n com n>1: ");
	scanf("%d",&n);
	printf("\nAdicione o valor do limite inferior da integral: ");
	scanf("%lf",&a);
	printf("\nAdicione o valor do limite superior da integral: ");
	scanf("%lf",&b);
	
	/* aplicando o metodo da regra do trapézio */
	h=fabs(b-a)/n; /* a função fabs (math.h) retorna o valor absoluto. Ex.: fabs (x) = \x\ */
	
	/* laço de repetição para o cálculo */
	for(i=1;i<n;i++){
		x=a+i*h; 
		val_int=val_int+f(x);
	}
	
	/* cálculo final para o valor do resultado da integral */
	integral=(h/2)*(f(a)+f(b)+2*val_int);
	/* imprime o valor */
	printf("\nThe integral is: %lf\n",integral);
}
  
