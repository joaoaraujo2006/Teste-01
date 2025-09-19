
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    dados = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot

    plt.figure(figsize=(10, 6))
    plt.scatter(dados["Year"], dados["CSIRO Adjusted Sea Level"], label="Dados observados", alpha=0.7)

    # Create first line of best fit

    inclinacao, intercepto, r, p, erro_padrao = linregress(dados["Year"], dados["CSIRO Adjusted Sea Level"])
    anos = range(dados["Year"].min(), 2051)
    plt.plot(anos, intercepto + inclinacao * pd.Series(anos), "r", label="Tendência (todos os anos)")

    # Create second line of best fit

    dadosRecentes = dados[dados["Year"] >= 2000]
    resultado = linregress(dadosRecentes["Year"], dadosRecentes["CSIRO Adjusted Sea Level"])
    inclinacaoRecente = resultado.slope
    interceptoRecente = resultado.intercept
    anos_recentes_extendidos = range(2000, 2051)
    plt.plot(anos_recentes_extendidos,interceptoRecente + inclinacaoRecente * pd.Series(anos_recentes_extendidos),"g", label="Tendência (2000 em diante)")
    
    # Add labels and title

    plt.xlabel("Ano")
    plt.ylabel("Nível do mar (polegadas)")
    plt.title("Elevação do nível do mar")
    plt.legend()
    plt.grid(True)
    plt.savefig('sea_level_plot.png')
    plt.show()

    
    
    # Save plot and return data for testing (DO NOT MODIFY)
