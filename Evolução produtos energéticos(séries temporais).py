import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima_model import ARIMA

''' Aqui vamos fazer uma série temporal com a produção de produtos energéticos derivados do petróleo para os anos de 2019 e 2020.
    Produtos energéticos - Gasolina Aditivada, Gasolina de aviação, GLP1(Gás Liquefeto de Petróleo), Óleo combustível, Óleo diesel, QAV(Querosene de Aviação), Querosene iluminante, Outros.'''

#banco de dados original
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';')

'''Agora faremos a separação dos produtos energéticos derivados do petróleo.
   1) Faremos a separação dos produtos energéticos usando uma lista para colocarmos num laço.
   2) Iremos ajustar os novos dataframes desmembrado do dataframe inicial
   3) Transformaremos as listas em novos dataframes
   4) Alteração nos nomes das colunas para o mesmo do dataframe inicial'''

# 1º Passo
energetico = []

# 2º Passo
for index, column in dados.iterrows():
    if column['Tipo de Derivado'] == 'Energético':
        e = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        energetico.append(e)

# 3º Passo
energetico =  pd.DataFrame(list(energetico))

# 4º Passo
energetico.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']

#Precisaremos fazer a transformação dos números da coluna 'produção (m³)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
energetico['Produção (m³)'] = energetico['Produção (m³)'].str.replace(",", ".").astype(float)

#Agora faremos a soma total da produção de todos os produtos energéticos para cada ano, e transforma-los em dataframe.
energetico = energetico.groupby(['Ano'])['Produção (m³)'].sum().to_frame()

#Vamos exportar esse novo dataframe para transforma-lo em arquivo CSV
energetico.to_csv(r'D:\Meus Documentos\Desktop\Projetos Cientista de Dados\serie_temporal_energetico.csv')

#Novo banco de dados com o somatório total dos produtos energéticos de cada ano
dados2 = pd.read_csv('D:\\Meus Documentos\\Desktop\\Projetos Cientista de Dados\\G2.19 - Distribuição percentual da produção de derivados de petróleo não energéticos – 2018\\serie_temporal_energetico.csv')

print(dados2.dtypes)

#Precisamos transformar o ano do tipo 'object' para o ano tipo data para ser aplicada na série temporal
dateparse = lambda dates:pd.datetime.strptime(dates, '%Y')

#Fazendo a alteração do index no banco de dados para receber os anos da série temporal
dados2 = pd.read_csv('D:\\Meus Documentos\\Desktop\\Projetos Cientista de Dados\\G2.19 - Distribuição percentual da produção de derivados de petróleo não energéticos – 2018\\serie_temporal_energetico.csv',
                     parse_dates = ['Ano'], index_col = 'Ano', date_parser = dateparse)

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

modelo = ARIMA(dados2, order = [0, 0, 1])
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