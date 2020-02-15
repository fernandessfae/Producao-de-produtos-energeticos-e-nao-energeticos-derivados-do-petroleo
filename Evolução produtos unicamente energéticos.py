import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de produtos unicamente energéticos derivados do petróleo entre os anos de 2009 a 2018, e fazer a sua comparação (isolados e juntos).
    Produtos energéticos - Gasolina Aditivada, Gasolina de aviação, GLP1(Gás Liquefeto de Petróleo), Óleo combustível, Óleo diesel, QAV(Querosene de Aviação), Querosene iluminante, Outros.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

#Criação de uma lista para a separação de produtos energeticos derivado do petróleo
gasolina_aditivada = []
gasolina_aviacao = []
glp = []
oleo_combustivel = []
oleo_diesel = []
qi = []
qav = []
outros = []

for index, column in dados.iterrows():
    if column['Derivados de petróleo'] == 'Gasolina A ':
        gad = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        gasolina_aditivada.append(gad)
    elif column['Derivados de petróleo'] == 'Gasolina de aviação':
        gav = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        gasolina_aviacao.append(gav)
    elif column['Derivados de petróleo'] == 'GLP1':
        glp1 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        glp.append(glp1)
    elif column['Derivados de petróleo'] == 'Óleo combustível2,3':
        olc = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        oleo_combustivel.append(olc)
    elif column['Derivados de petróleo'] == 'Óleo diesel3':
        old = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        oleo_diesel.append(old)
    elif column['Derivados de petróleo'] == 'QAV':
        qav1 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        qav.append(qav1)
    elif column['Derivados de petróleo'] == 'Querosene iluminante':
        qil = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        qi.append(qil)
    elif column['Derivados de petróleo'] == 'Outros4':
        ot = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        outros.append(ot)

#Transformação das listas em dataframe
gasolina_aditivada = pd.DataFrame(list(gasolina_aditivada))
gasolina_aviacao = pd.DataFrame(list(gasolina_aviacao))
glp = pd.DataFrame(list(glp))
oleo_combustivel = pd.DataFrame(list(oleo_combustivel))
oleo_diesel = pd.DataFrame(list(oleo_diesel))
qi = pd.DataFrame(list(qi))
qav = pd.DataFrame(list(qav))
outros = pd.DataFrame(list(outros))

#Renomeação das colunas dos dataframes recém-criados
gasolina_aditivada.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
gasolina_aviacao.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
glp.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
oleo_combustivel.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
oleo_diesel.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
qi.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
qav.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
outros.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']

#Plotando o gráfico da gasolina aditivada
plt.bar(gasolina_aditivada.iloc[:, 2], gasolina_aditivada.iloc[:, 3], color = 'blue')
plt.xticks(gasolina_aditivada['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^7 m³)')
plt.title('Produção de gasolina aditivada (2009 - 2018)')

#Plotando o gráfico da gasolina de aviação
plt.bar(gasolina_aviacao.iloc[:, 2], gasolina_aviacao.iloc[:, 3], color = 'red')
plt.xticks(gasolina_aviacao['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de gasolina de aviação (2009 - 2018)') 

#Plotando o gráfico de gás liquefeto de petróleo (GLP)
plt.bar(glp.iloc[:, 2], glp.iloc[:, 3], color = 'yellow')
plt.xticks(glp['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^7 m³)')
plt.title('Produção de gás liquefeto de petróleo - GLP (2009 - 2018)')

#Plotando o gráfico de óleo de combustível
plt.bar(oleo_combustivel.iloc[:, 2], oleo_combustivel.iloc[:, 3], color = 'orange')
plt.xticks(oleo_combustivel['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^7 m³)')
plt.title('Produção de óleo de combustível (2009 - 2018)') 

#Plotando o gráfico de óleo diesel
plt.bar(oleo_diesel.iloc[:, 2], oleo_diesel.iloc[:, 3], color = 'green')
plt.xticks(oleo_diesel['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^7 m³)')
plt.title('Produção de óleo de combustível (2009 - 2018)')

#Plotando o gráfico de óleo de querosene iluminante
plt.bar(qi.iloc[:, 2], qi.iloc[:, 3], color = 'brown')
plt.xticks(qi['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de querosene iluminante (2009 - 2018)')

#Plotando o gráfico de óleo de querosene de aviação
plt.bar(qav.iloc[:, 2], qav.iloc[:, 3], color = 'black')
plt.xticks(qav['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de querosene de aviação (2009 - 2018)')

#Plotando o gráfico de outros produtos energéticos
plt.bar(outros.iloc[:, 2], outros.iloc[:, 3], color = 'purple')
plt.xticks(outros['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de outros produtos energéticos (2009 - 2018)')

#Plotando o gráfico comparando todos os produtos energéticos
barWidth = 0.1
plt.figure(figsize = (10, 5))
r1 = np.arange(len(gasolina_aditivada.iloc[:, 2]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]
r8 = [x + barWidth for x in r7]
plt.bar(r1, gasolina_aditivada.iloc[:, 3], color = '#00008B', width = barWidth, label = 'Gasolina Aditivada')
plt.bar(r2, gasolina_aviacao.iloc[:, 3], color = '#0000CD', width = barWidth, label = 'Gasolina Aviação')
plt.bar(r3, glp.iloc[:, 3], color = '#0000FF', width = barWidth, label = 'Gas Liquefeto de Petróleo')
plt.bar(r4, oleo_combustivel.iloc[:, 3], color = '#6495ED', width = barWidth, label = 'Óleo de Combustível')
plt.bar(r5, oleo_diesel.iloc[:, 3], color = '#4169E1', width = barWidth, label = 'Óleo Diesel')
plt.bar(r6, qi.iloc[:, 3], color = '#1E90FF', width = barWidth, label = 'Querosene Iluminante')
plt.bar(r7, qav.iloc[:, 3], color = '#00BFFF', width = barWidth, label = 'Querosene de Aviação')
plt.bar(r8, outros.iloc[:, 3], color = '#87CEFA', width = barWidth, label = 'Outros Energéticos')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(gasolina_aditivada.iloc[:, 3]))], gasolina_aditivada['Ano'])
plt.ylabel('Total Produção Anual (10^7 m³)')
plt.title('Produção de produtos unicamente energéticos derivados do petróleo (2009 - 2018)')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
