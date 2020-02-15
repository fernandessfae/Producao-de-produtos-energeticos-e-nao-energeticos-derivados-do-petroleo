import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de produtos unicamente não energéticos derivados do petróleo entre os anos de 2009 a 2018.
    Produtos não energéticos - Asfalto, Coque, Nafta, Óleo Lubrificante, Parafina, Solvente, Outros.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

# Separação dos produtos não energéticos
asfalto = []
coque = []
nafta = []
oleo_lubrificante = []
parafina = []
solvente = []
outros = []

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

# Transformação das listas em dataframes
asfalto = pd.DataFrame(list(asfalto))
coque = pd.DataFrame(list(coque))
nafta = pd.DataFrame(list(nafta))
oleo_lubrificante = pd.DataFrame(list(oleo_lubrificante))
parafina = pd.DataFrame(list(parafina))
solvente = pd.DataFrame(list(solvente))
outros = pd.DataFrame(list(outros))

# Renomeação das colunas das listas recém criadas
asfalto.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
coque.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
nafta.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
oleo_lubrificante.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
parafina.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
solvente.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
outros.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']

#Plotando o gráfico do asfalto
plt.bar(asfalto.iloc[:, 2], asfalto.iloc[:, 3], color = 'blue')
plt.xticks(asfalto['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de asfalto (2009 - 2018)')

#Plotando o gráfico do coque
plt.bar(coque.iloc[:, 2], coque.iloc[:, 3], color = 'red')
plt.xticks(coque['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de coque (2009 - 2018)')

#Plotando o gráfico da nafta
plt.bar(nafta.iloc[:, 2], nafta.iloc[:, 3], color = 'yellow')
plt.xticks(nafta['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de coque (2009 - 2018)')

#Plotando o gráfico do óleo lubrificante
plt.bar(oleo_lubrificante.iloc[:, 2], oleo_lubrificante.iloc[:, 3], color = 'orange')
plt.xticks(oleo_lubrificante['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de coque (2009 - 2018)')

#Plotando o gráfico da parafina
plt.bar(parafina.iloc[:, 2], parafina.iloc[:, 3], color = 'green')
plt.xticks(parafina['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de coque (2009 - 2018)')

#Plotando o gráfico do solvente
plt.bar(solvente.iloc[:, 2], solvente.iloc[:, 3], color = 'brown')
plt.xticks(solvente['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de coque (2009 - 2018)')

#Plotando o gráfico de outros não produtos energéticos
plt.bar(outros.iloc[:, 2], outros.iloc[:, 3], color = 'purple')
plt.xticks(outros['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de outros produtos energéticos (2009 - 2018)')

#Plotando o gráfico comparando todos os produtos não energéticos
barWidth = 0.1
plt.figure(figsize = (10, 5))
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
plt.bar(r7, outros.iloc[:, 3], color = '#5F9EA0', width = barWidth, label = 'Outros Energéticos')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(asfalto.iloc[:, 3]))], asfalto['Ano'])
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de produtos unicamente não energéticos derivados do petróleo (2009 - 2018)')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
