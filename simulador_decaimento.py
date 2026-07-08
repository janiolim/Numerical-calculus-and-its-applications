import numpy as np
import matplotlib.pyplot as plt

"""
Sistema de Energia Nuclear Regional (SENR)
Módulo: Física Nuclear Aplicada
Script: Simulador de Decaimento Radioativo e Atividade do Combustível
"""

def calcular_decaimento(n0, meia_vida, tempo_maximo, passos):
    """
    Calcula a curva de decaimento de um isótopo radioativo.
    """
    # Calcula a constante de decaimento (lambda)
    constante_lambda = np.log(2) / meia_vida
    
    # Cria um vetor de tempo de 0 até tempo_maximo
    tempo = np.linspace(0, tempo_maximo, passos)
    
    # Aplica a equação N(t) = N0 * e^(-lambda * t)
    quantidade_restante = n0 * np.exp(-constante_lambda * tempo)
    
    return tempo, quantidade_restante

if __name__ == "__main__":
    print("--- SENR: Simulador de Decaimento Radioativo ---")
    
    # Parâmetros de entrada (Exemplo: Urânio-235 ou outro isótopo de interesse)
    # Para visualização rápida, vamos simular um isótopo com meia-vida fictícia de 30 anos
    n0 = float(input("Quantidade inicial de material (em kg): "))
    meia_vida = float(input("Tempo de meia-vida do isótopo (em anos): "))
    tempo_simulacao = float(input("Tempo total de simulação (em anos): "))
    
    # Gerando os dados
    tempos, quantidades = calcular_decaimento(n0, meia_vida, tempo_simulacao, 500)
    
    # Exibindo resultados no terminal
    quantidade_final = quantidades[-1]
    print(f"\nApós {tempo_simulacao} anos, restarão aproximadamente {quantidade_final:.2f} kg do material inicial.")
    
    # Plotando o gráfico (O grande trunfo do Python!)
    plt.figure(figsize=(10, 6))
    plt.plot(tempos, quantidades, label=f'Decaimento (Meia-vida: {meia_vida} anos)', color='#D32F2F', linewidth=2.5)
    
    plt.title('SENR - Curva de Decaimento Radioativo', fontsize=14, fontweight='bold')
    plt.xlabel('Tempo (Anos)', fontsize=12)
    plt.ylabel('Quantidade de Material (kg)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.fill_between(tempos, quantidades, color='#D32F2F', alpha=0.1) # Sombreamento elegante
    plt.legend()
    
    # Salva o gráfico como imagem (ótimo para colocar no Readme do GitHub)
    plt.savefig('grafico_decaimento.png', dpi=300, bbox_inches='tight')
    print("Gráfico salvo como 'grafico_decaimento.png'. Feche a janela do gráfico para encerrar.")
    
    plt.show()
