import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA

''' Aqui vamos fazer uma série temporal com a produção total de produtos energéticos derivados do petróleo para os anos de 2019 e 2020.'''

energetico = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',', index_col = 'Tipo de Derivado')

#Remove linhas e colunas desnecessárias para a previsão total dos produtos energéticos
energetico = energetico.drop('Não energético')
energetico = energetico.drop('Derivados de petróleo', axis = 1)

#Renomeação da coluna produção
energetico = energetico.rename(columns = {'Produção (m3)' : 'Produção (m³)'})

#Agora faremos a soma total da produção de todos os produtos energéticos para cada ano
energetico = energetico.groupby(['Ano'])['Produção (m³)'].sum().reset_index()

#Tranforma a coluna para o tipo de tempo
energetico['Ano'] = pd.to_datetime(energetico['Ano'].astype(str), format = '%Y')

#Tranforma a coluna temporal em índice
energetico = energetico.set_index('Ano')

#Plotando o gráfico da produção total de produtos energéticos do petróleo durante os anos de 2009 a 2018
plt.figure(figsize = (10, 5))
plt.title('Produção total de todos os produtos energéticos')
plt.xlabel('Anos')
plt.ylabel('Quantidade (m³)')
plt.plot(energetico)

#Agora iremos definir varíaveis para ver se há tendência, sazionalidade e o resíduo 
decomposicao = seasonal_decompose(energetico)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid

#Iremos agora plotar os gráficos original, tendência, sazionalidade e resíduo
plt.subplot(4, 1, 1)
plt.plot(energetico, label = 'Original')
plt.legend(loc = 'best')

plt.subplot(4, 1, 2)
plt.plot(tendencia, label = 'Tendência')
plt.legend(loc = 'best')

plt.subplot(4, 1, 3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')

plt.subplot(4, 1, 4)
plt.plot(aleatorio, label = 'Aleatório')
plt.legend(loc = 'best')
plt.tight_layout()

#cria um modelo para determinar o AUTOARIMA
modelo_auto = auto_arima(energetico, m = 2, seasonal = False, trace = True)

#detalha todos os parâmetros do ARIMA
modelo_auto.summary() 

#Fazer uma previsao com auto ARIMA com o número de previsões
proximo_ano = modelo_auto.predict(n_periods = 2)

#Agora será construido o modelo de previsão com o ARIMA escolhido anteriormente e iremos treina-lo
modelo = ARIMA(energetico, order = [0, 0, 1])
modelo_treinado = modelo.fit()

#visualizar os detalhes/parâmetros do modelo
modelo_treinado.summary()

#Cria uma previsão da série temporal, passando quantas previsoes que queremos adiante (steps)
previsoes = modelo_treinado.forecast(steps = 2)[0]

#Plota o gráfico da previsão de 2018 a 2020
eixo = energetico.plot()
modelo_treinado.plot_predict('2009-01-01', '2020-01-01', ax = eixo, plot_insample = False)
