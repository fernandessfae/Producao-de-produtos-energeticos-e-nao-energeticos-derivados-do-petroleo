import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de produtos energéticos e não energéticos derivados do petróleo entre os anos de 2009 a 2018, e fazer a sua comparação (isolados e juntos).'''

dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

#Separação dos produtos energéticos e não energéticos
energetico, nao_energetico = ([] for i in range(2))

for index, column in dados.iterrows():
    if column['Tipo de Derivado'] == 'Energético':
        e = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        energetico.append(e)
    else:
        ne = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        nao_energetico.append(ne) 

#Criação de uma função para transformar as listas em dataframes
def dataframe(x):
    x =  pd.DataFrame(list(x))
    x.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
    x = x.groupby(['Ano'])['Produção (m³)'].sum().reset_index()
    return x

energetico = dataframe(energetico)
nao_energetico = dataframe(nao_energetico)

#Criação de uma função para visualização dos produtos derivados do petróleo
def histograma(x):
    plt.figure(figsize = (10, 5))
    plt.xticks(x['Ano'])
    plt.xlabel('Produção Anual')
    plt.ylabel('Quantidade (m³)')
    if x is energetico:
        plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'blue')
        plt.title('Produção de produtos energéticos derivados do petróleo')
    else:
        plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = '#ADD8E6')
        plt.title('Produção de produtos não energéticos derivados do petróleo')

histograma(energetico)
histograma(nao_energetico)

#Fazendo o gráfico para os produtos energéticos e não energéticos
barWidth = 0.4
plt.figure(figsize = (10, 5))
r1 = np.arange(len(energetico.iloc[:, 0]))
r2 = [x + barWidth for x in r1]
plt.bar(r1, energetico.iloc[:, 1], color = '#4169E1', width = barWidth, label = 'Energético')
plt.bar(r2, nao_energetico.iloc[:, 1], color = '#1E90FF', width = barWidth, label = 'Não Energético')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(energetico.iloc[:, 0]))], energetico['Ano'])
plt.ylabel('Quantidade (m³)')
plt.title('Produção de produtos energéticos e não energéticos derivados do petróleo')
plt.legend()
plt.show()       
