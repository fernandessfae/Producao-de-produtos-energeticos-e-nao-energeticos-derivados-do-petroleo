import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de produtos unicamente não energéticos derivados do petróleo entre os anos de 2009 a 2018.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

# Separação dos produtos não energéticos
asfalto, coque, nafta, oleo_lubrificante, parafina, solvente, outros = ([] for i in range(7))

for index, column in dados.iterrows():
    if column['Derivados de petróleo'] == 'Asfalto':
        asf = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        asfalto.append(asf)
    elif column['Derivados de petróleo'] == 'Coque5':
        coq = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        coque.append(coq)
    elif column['Derivados de petróleo'] == 'Nafta6':
        naf = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        nafta.append(naf)
    elif column['Derivados de petróleo'] == 'Óleo lubrificante ':
        oleo = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        oleo_lubrificante.append(oleo)
    elif column['Derivados de petróleo'] == 'Parafina':
        para = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        parafina.append(para)
    elif column['Derivados de petróleo'] == 'Solvente':
        sol = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        solvente.append(sol)
    elif column['Derivados de petróleo'] == 'Outros7':
        out = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        outros.append(out)

#Criação de uma função para transformar as listas em dataframes
def dataframe(x):
    x = pd.DataFrame(list(x))
    x.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
    return x

asfalto = dataframe(asfalto)
coque = dataframe(coque)
nafta = dataframe(nafta)
oleo_lubrificante = dataframe(oleo_lubrificante)
parafina = dataframe(parafina)
solvente = dataframe(solvente)
outros = dataframe(outros)

#Criação de uma função para a plotagem dos histogramas dos produtos não energéticos de petróleo
def histograma(x):
    plt.figure(figsize = (10, 5))
    plt.xticks(x['Ano'])
    plt.xlabel('Produção Anual')
    plt.ylabel('Quantidade (m³)')
    if x is asfalto:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'blue')
        plt.title('Produção total de asfalto')
    elif x is coque:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'red')
        plt.title('Produção total de coque')
    elif x is nafta:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'yellow')
        plt.title('Produção total de nafta')
    elif x is oleo_lubrificante:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'orange')
        plt.title('Produção total de óleo lubrificante')
    elif x is parafina:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'green')
        plt.title('Produção total de parafina')
    elif x is solvente:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'brown')
        plt.title('Produção total de solvente')
    else:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'purple')
        plt.title('Produção total de outros produtos não energéticos')

histograma(asfalto)
histograma(coque)
histograma(nafta)
histograma(oleo_lubrificante)
histograma(parafina)
histograma(solvente)
histograma(outros)

#Plotando o gráfico comparando todos os produtos não energéticos
barWidth = 0.1
plt.figure(figsize = (15, 5))
r1 = np.arange(len(asfalto.iloc[:, 2]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]
plt.bar(r1, asfalto.iloc[:, 3], color = '#00FFFF', width = barWidth, label = 'Asfalto')
plt.bar(r2, coque.iloc[:, 3], color = '#00CED1', width = barWidth, label = 'Coque')
plt.bar(r3, nafta.iloc[:, 3], color = '#40E0D0', width = barWidth, label = 'Nafta')
plt.bar(r4, oleo_lubrificante.iloc[:, 3], color = '#48D1CC', width = barWidth, label = 'Óleo lubrificante')
plt.bar(r5, parafina.iloc[:, 3], color = '#20B2AA', width = barWidth, label = 'Parafina')
plt.bar(r6, solvente.iloc[:, 3], color = '#008B8B', width = barWidth, label = 'Solvente')
plt.bar(r7, outros.iloc[:, 3], color = '#5F9EA0', width = barWidth, label = 'Outros Não Energéticos')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(asfalto.iloc[:, 3]))], asfalto['Ano'])
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de produtos unicamente não energéticos derivados do petróleo')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
