#include <stdio.h>
#include <math.h>


/* Algoritmo para Cálculo Numérico
   Método da Bisseção para encontrar raízes reais de funções */

/* Definindo a função f(x)
   Neste exemplo, vamos buscar a raiz de f(x) = x^3 - x - 2 */
double f(double x) {
	return (x * x * x) - x - 2.0;
}

int main() {
	double a, b, c;        /* a e b formam o intervalo, c é o ponto médio */
	double tol;            /* tolerância para o critério de parada */
	int iteracoes = 0;
	int max_iter = 100;    /* trava de segurança pro loop não rodar infinito */

	printf("--- Metodo da Bissecao ---\n");
	printf("Digite o valor de 'a' (limite inferior): ");
	scanf("%lf", &a);
	printf("Digite o valor de 'b' (limite superior): ");
	scanf("%lf", &b);
	printf("Digite a tolerancia (ex: 0.001): ");
	scanf("%lf", &tol);

	/* Pelo Teorema de Bolzano, f(a) e f(b) precisam ter sinais opostos
	   para garantir que a raiz cruza o eixo x no intervalo dado */
	if (f(a) * f(b) >= 0) {
		printf("\nErro: O intervalo nao garante uma raiz.\n");
		printf("Certifique-se de que f(a) e f(b) tenham sinais diferentes.\n");
		return 1;
	}

	/* Laço principal da bisseção */
	do {
		c = (a + b) / 2.0; /* encontra o meio do caminho */
		iteracoes++;

		/* verifica de qual lado a raiz está para encurtar o intervalo */
		if (f(a) * f(c) < 0) {
			b = c; /* a raiz está na metade esquerda */
		} else {
			a = c; /* a raiz está na metade direita */
		}

	} while (fabs(b - a) >= tol && iteracoes < max_iter);

	/* Imprime os resultados finais */
	printf("\nRaiz aproximada encontrada: %lf\n", c);
	printf("Numero de iteracoes: %d\n", iteracoes);

	return 0;
}
