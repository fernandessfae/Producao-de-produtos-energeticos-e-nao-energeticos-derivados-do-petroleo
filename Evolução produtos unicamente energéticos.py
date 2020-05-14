import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de produtos unicamente energéticos derivados do petróleo entre os anos de 2009 a 2018, e fazer a sua comparação (isolados e juntos).'''

energetico = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

#Criação de uma lista para a separação de produtos energeticos derivado do petróleo
gasolina_aditivada, gasolina_aviacao, glp, oleo_combustivel, oleo_diesel, qi, qav, outros = ([] for i in range(8))

for index, column in energetico.iterrows():
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

#Criação de uma função para transformar as listas em dataframes
def dataframe(x):
    x = pd.DataFrame(list(x))
    x.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
    return x

gasolina_aditivada = dataframe(gasolina_aditivada)
gasolina_aviacao = dataframe(gasolina_aviacao)
glp = dataframe(glp)
oleo_combustivel = dataframe(oleo_combustivel)
oleo_diesel = dataframe(oleo_diesel)
qi = dataframe(qi)
qav = dataframe(qav)
outros = dataframe(outros)

#Criação de uma função para a plotagem dos histogramas dos produtos energéticos de petróleo
def histograma(x):
    plt.figure(figsize = (10, 5))
    plt.xticks(x['Ano'])
    plt.xlabel('Produção Anual')
    plt.ylabel('Quantidade (m³)')
    if x is gasolina_aditivada:
        plt.title('Produção total de gasolina aditivada')
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'blue')
    elif x is gasolina_aviacao:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'red')
        plt.title('Produção total de gasolina de aviação')
    elif x is glp:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'yellow')
        plt.title('Produção total de gás liquefeto de petróleo - GLP')
    elif x is oleo_combustivel:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'orange')
        plt.title('Produção total de óleo de combustível')
    elif x is oleo_diesel:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'green')
        plt.title('Produção total de óleo diesel')
    elif x is qi:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'brown')
        plt.title('Produção total de querosene iluminante')
    elif x is qav:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'purple')
        plt.title('Produção total de querosene de aviação')
    else:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'black')
        plt.title('Produção total de outros produtos energéticos')

histograma(gasolina_aditivada)
histograma(gasolina_aviacao)
histograma(glp)
histograma(oleo_combustivel)
histograma(oleo_diesel)
histograma(qi)
histograma(qav)
histograma(outros)

#Plotando o gráfico comparando todos os produtos energéticos
barWidth = 0.1
plt.figure(figsize = (15, 5))
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
plt.ylabel('Quantidade (m³)')
plt.title('Produção de produtos unicamente energéticos derivados do petróleo')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
