import pandas as pd
import matplotlib.pyplot as plt

''' Aqui vamos fazer um histograma com a produção  total de produtos energéticos e não energéticos derivados do petróleo entre os anos de 2009 a 2018.'''

total = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',', index_col = 'Tipo de Derivado')

#Remove linhas e colunas desnecessárias para a previsão total dos produtos energéticos
total = total.drop('Derivados de petróleo', axis = 1)

#Renomeação da coluna produção
total = total.rename(columns = {'Produção (m3)' : 'Produção (m³)'})

#Agora faremos a soma total da produção de todos os produtos energéticos e não energéticos para cada ano
total = total.groupby(['Ano'])['Produção (m³)'].sum().reset_index()

#Fazendo o gráfico para a produção anual total.
plt.figure(figsize = (10, 5))
plt.bar(total.iloc[:, 0], total.iloc[:, 1], color = '#7FFFD4')
plt.xticks(total['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Quantidade (m³)')
plt.title('Produção total de produtos energéticos e não energéticos derivados do petróleo')
