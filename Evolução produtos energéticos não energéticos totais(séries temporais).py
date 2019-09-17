import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima_model import ARIMA

''' Aqui vamos fazer uma série temporal com a produção de produtos energéticos não energéticos derivados do petróleo para os anos de 2019 e 2020.
    Produtos energéticos - Gasolina Aditivada, Gasolina de aviação, GLP1(Gás Liquefeto de Petróleo), Óleo combustível, Óleo diesel, QAV(Querosene de Aviação), Querosene iluminante, Outros.
    Produtos não energéticos - Asfalto, Coque, Nafta, Óleo Lubrificante, Parafina, Solvente, Outros.'''

#banco de dados original
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';')

'''Agora faremos a separação dos produtos não energéticos derivados do petróleo.
   1) Faremos a separação dosprodutos não energéticos usando uma lista para colocarmos num laço.
   2) Iremos ajustar os novos dataframes desmembrado do dataframe inicial
   3) Transformaremos as listas em novos dataframes
   4) Alteração nos nomes das colunas para o mesmo do dataframe inicial'''

# 1º Passo
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

# 2º Passo
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

# 3º Passo
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

# 4º Passo
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

#Precisaremos fazer a transformação dos números da coluna 'produção (m³)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
ano_2009['Produção (m³)'] = ano_2009['Produção (m³)'].str.replace(",", ".").astype(float)
ano_2010['Produção (m³)'] = ano_2010['Produção (m³)'].str.replace(",", ".").astype(float)
ano_2011['Produção (m³)'] = ano_2011['Produção (m³)'].str.replace(",", ".").astype(float)
ano_2012['Produção (m³)'] = ano_2012['Produção (m³)'].str.replace(",", ".").astype(float)
ano_2013['Produção (m³)'] = ano_2013['Produção (m³)'].str.replace(",", ".").astype(float)
ano_2014['Produção (m³)'] = ano_2014['Produção (m³)'].str.replace(",", ".").astype(float)
ano_2015['Produção (m³)'] = ano_2015['Produção (m³)'].str.replace(",", ".").astype(float)
ano_2016['Produção (m³)'] = ano_2016['Produção (m³)'].str.replace(",", ".").astype(float)
ano_2017['Produção (m³)'] = ano_2017['Produção (m³)'].str.replace(",", ".").astype(float)
ano_2018['Produção (m³)'] = ano_2018['Produção (m³)'].str.replace(",", ".").astype(float)

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

#Vamos exportar esse novo dataframe para transforma-lo em arquivo CSV
ano_total.to_csv(r'D:\Meus Documentos\Desktop\Projetos Cientista de Dados\G2.19 - Distribuição percentual da produção de derivados de petróleo não energéticos – 2018\serie_temporal_energetico_nao_energetico.csv')

#Novo banco de dados com o somatório total dos produtos energeticos e não energéticos de cada ano
dados2 = pd.read_csv('D:\\Meus Documentos\\Desktop\\Projetos Cientista de Dados\\G2.19 - Distribuição percentual da produção de derivados de petróleo não energéticos – 2018\\serie_temporal_energetico_nao_energetico.csv')

print(dados2.dtypes)

#Precisamos transformar o ano do tipo 'object' para o ano tipo data para ser aplicada na série temporal
dateparse = lambda dates:pd.datetime.strptime(dates, '%Y')

#Fazendo a alteração do index no banco de dados para receber os anos da série temporal
dados2 = pd.read_csv('D:\\Meus Documentos\\Desktop\\Projetos Cientista de Dados\\G2.19 - Distribuição percentual da produção de derivados de petróleo não energéticos – 2018\\serie_temporal_energetico_nao_energetico.csv',
                     parse_dates = ['Ano'], index_col = 'Ano', date_parser = dateparse)

#Remover a primeira coluna do dataframe
dados2 = dados2.drop('Unnamed: 0', axis = 1)

#cria o gráfico da série temporal original
plt.plot(dados2)

#cria um modelo para determinar o ARIMA
modelo_auto = auto_arima(dados2, m = 2, seasonal = False, trace = True)

#detalha todos os parâmetros do ARIMA
modelo_auto.summary()

#Fazer uma previsao com auto ARIMA com o número de previsões
proximo_ano = modelo_auto.predict(n_periods = 2)

'''Criar uma variavel com o parâmetros do ARIMA adquiridos com o auto arima, passando o banco de dados e ajustando no modelo
   Lembrando que o auto ARIMA determina varios parâmetros, e maquina escolhe o mais apropriado para ela, entretanto é importante
   testar outros parâmetros para ver como se sai o gráfico da série temporal.'''
   
modelo = ARIMA(dados2, order = [1, 0, 0])
modelo_treinado = modelo.fit()

#visualizar os detalhes/parâmetros do modelo
modelo_treinado.summary()

#Cria uma previsão da série temporal, passando quantas previsoes que queremos adiante (steps)
previsoes = modelo_treinado.forecast(steps = 2)[0]

#Gera um gráfico com as previsoes, comparando com a série original
eixo = dados2.plot()
modelo_treinado.plot_predict('2009-01-01', '2020-01-01', ax = eixo, plot_insample = False)

''' Obs¹: tanto a váriavel 'proximo_ano' e 'previsoes' irao fazer as previsoes posteriores
    e poderão dar valores diferentes, em virtude do AUTO ARIMA já utilizar algumas configurações
    extras para utilizar no seu modelo.
    
    Obs²: no gráfico há a linha do gráfico real e da previsão da máquina, e como a base de dados
    tem poucos dados, é normal as linhas ficarem um pouco distantes.'''