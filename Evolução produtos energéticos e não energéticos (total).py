import pandas as pd
import matplotlib.pyplot as plt

''' Aqui vamos fazer um histograma com a produção  total de produtos energéticos e não energéticos derivados do petróleo entre os anos de 2009 a 2018.
    Produtos energéticos - Gasolina Aditivada, Gasolina de aviação, GLP1(Gás Liquefeto de Petróleo), Óleo combustível, Óleo diesel, QAV(Querosene de Aviação), Querosene iluminante, Outros.
    Produtos não energéticos - Asfalto, Coque, Nafta, Óleo Lubrificante, Parafina, Solvente, Outros.'''

#Carregamento da base de dados
dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

#Separação dos derivados de petróleo por ano
ano_2009 = []
ano_2010 = []
ano_2011 = []
ano_2012 = []
ano_2013 = []
ano_2014 = []
ano_2015 = []
ano_2016 = []
ano_2017 = []
ano_2018 = []

for index, column in dados.iterrows():
    if column['Ano'] == 2009:
        a2009 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2009.append(a2009)
    elif column['Ano'] == 2010:
        a2010 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2010.append(a2010)
    elif column['Ano'] == 2011:
        a2011 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2011.append(a2011)
    elif column['Ano'] == 2012:
        a2012 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2012.append(a2012)
    elif column['Ano'] == 2013:
        a2013 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2013.append(a2013)
    elif column['Ano'] == 2014:
        a2014 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2014.append(a2014)
    elif column['Ano'] == 2015:
        a2015 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2015.append(a2015)
    elif column['Ano'] == 2016:
        a2016 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2016.append(a2016)
    elif column['Ano'] == 2017:
        a2017 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2017.append(a2017)
    else:
        a2018 = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        ano_2018.append(a2018)

# Transformação das listas em dataframe
ano_2009 = pd.DataFrame(list(ano_2009))
ano_2010 = pd.DataFrame(list(ano_2010))
ano_2011 = pd.DataFrame(list(ano_2011))
ano_2012 = pd.DataFrame(list(ano_2012))
ano_2013 = pd.DataFrame(list(ano_2013))
ano_2014 = pd.DataFrame(list(ano_2014))
ano_2015 = pd.DataFrame(list(ano_2015))
ano_2016 = pd.DataFrame(list(ano_2016))
ano_2017 = pd.DataFrame(list(ano_2017))
ano_2018 = pd.DataFrame(list(ano_2018))

# Colocação dos nomes das colunas de cada ano
ano_2009.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
ano_2010.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
ano_2011.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
ano_2012.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
ano_2013.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
ano_2014.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
ano_2015.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
ano_2016.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
ano_2017.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
ano_2018.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']

#Agora faremos a soma total da produção de todos os produtos energéticos e não energéticos para cada ano.
ano_2009 = ano_2009.groupby(['Ano'])['Produção (m³)'].sum()
ano_2010 = ano_2010.groupby(['Ano'])['Produção (m³)'].sum()
ano_2011 = ano_2011.groupby(['Ano'])['Produção (m³)'].sum()
ano_2012 = ano_2012.groupby(['Ano'])['Produção (m³)'].sum()
ano_2013 = ano_2013.groupby(['Ano'])['Produção (m³)'].sum()
ano_2014 = ano_2014.groupby(['Ano'])['Produção (m³)'].sum()
ano_2015 = ano_2015.groupby(['Ano'])['Produção (m³)'].sum()
ano_2016 = ano_2016.groupby(['Ano'])['Produção (m³)'].sum()
ano_2017 = ano_2017.groupby(['Ano'])['Produção (m³)'].sum()
ano_2018 = ano_2018.groupby(['Ano'])['Produção (m³)'].sum()

#Faremos uma nova lista para receber a produção total de cada ano.
ano_total = [ano_2009, ano_2010, ano_2011, ano_2012, ano_2013, ano_2014, ano_2015, ano_2016, ano_2017, ano_2018]

#Transformar os números de cada série anual numa lista com a produção anual
ano_total = [float(i) for i in ano_total]

#Tranformar a lista num dataframe
ano_total = pd.DataFrame(list(ano_total))

#Renomear a coluna 0 por 'Produção Anual'
ano_total = ano_total.rename(columns = {0 : 'Produção Anual'})

#Adiciona uma nova coluna com os anos correspondentes a sua produção.
ano_total['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

#Fazendo o gráfico para a produção anual total.
plt.bar(ano_total.iloc[:, 1], ano_total.iloc[:, 0], color = '#7FFFD4')
plt.xticks(ano_total['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^8 m³)')
plt.title('Produção total de produtos energéticos e não energéticos derivados do petróleo (2009 - 2018)')
