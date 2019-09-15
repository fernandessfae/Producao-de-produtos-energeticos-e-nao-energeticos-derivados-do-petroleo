import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de produtos energéticos e não energéticos derivados do petróleo entre os anos de 2009 a 2018, e fazer a sua comparação (isolados e juntos).
    Produtos energéticos - Gasolina Aditivada, Gasolina de aviação, GLP1(Gás Liquefeto de Petróleo), Óleo combustível, Óleo diesel, QAV(Querosene de Aviação), Querosene iluminante, Outros.
    Produtos não energéticos - Asfalto, Coque, Nafta, Óleo Lubrificante, Parafina, Solvente, Outros.'''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';')

'''Agora faremos a separação dos produtos energéticos e não energéticos derivados do petróleo.
   1) Faremos a separação dos energéticos e não energéticos usando uma lista para colocarmos num laço.
   2) Iremos ajustar os novos dataframes desmembrado do dataframe inicial
   3) Transformaremos as listas em novos dataframes
   4) Alteração nos nomes das colunas para o mesmo do dataframe inicial'''

# 1º Passo
energetico = []
nao_energetico = []

# 2º Passo
for index, column in dados.iterrows():
    if column['Tipo de Derivado'] == 'Energético':
        e = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        energetico.append(e)
    else:
        ne = column['Tipo de Derivado'], column['Derivados de petróleo'], column['Ano'], column['Produção (m3)']
        nao_energetico.append(ne) 

# 3º Passo
energetico =  pd.DataFrame(list(energetico))
nao_energetico =  pd.DataFrame(list(nao_energetico))

# 4º Passo
energetico.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
nao_energetico.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']

# Com ambos os comandos, iremos ver o tipo de cada coluna
print(energetico.dtypes)
print(nao_energetico.dtypes)

#Precisaremos fazer a transformação dos números da coluna 'produção (m³)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
energetico['Produção (m³)'] = energetico['Produção (m³)'].str.replace(",", ".").astype(float)
nao_energetico['Produção (m³)'] = nao_energetico['Produção (m³)'].str.replace(",", ".").astype(float)  

#Agora faremos a soma total da produção de todos os produtos energéticos e não energéticos para cada ano, e transforma-los em dataframe.
energetico_total = energetico.groupby(['Ano'])['Produção (m³)'].sum().to_frame()
nao_energetico_total = nao_energetico.groupby(['Ano'])['Produção (m³)'].sum().to_frame() 

#Adicionar uma coluna com todos os anos, igualando aos valores somados anteriormente
energetico_total['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
nao_energetico_total['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

#Fazendo o gráfico para os produtos energéticos
plt.bar(energetico_total.iloc[:, 1], energetico_total.iloc[:, 0], color = 'blue')
plt.xticks(energetico_total['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^8 m³)')
plt.title('Produção de produtos energéticos derivados do petróleo (2009 - 2018)')

#Fazendo o gráfico para os produtos não energéticos
plt.bar(nao_energetico_total.iloc[:, 1], nao_energetico_total.iloc[:, 0], color = '#ADD8E6')
plt.xticks(nao_energetico_total['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^7 m³)')
plt.title('Produção de produtos não energéticos derivados do petróleo (2009 - 2018)')

'''Explicando os parâmetros para explicar os gráficos acima:
    xticks() - Com ele definimos as labels do eixo X, ele precisa de um parâmetro com tipo de array que determine as labels.
    xlabel() e ylabel() - Com estes dois métodos adicionamos as labels do eixo Y e X, respectivamente.
    title() - adiciona o título do gráfico.
    plt.bar() - este método da lib plt, inicia a construsção do gráfico de barra, e aí começamos a passar os argumentos, que em ordem são:
            x: As coordernadas das barras do eixo X, que no nosso caso são as faixas etárias;
            height: A ‘altura’ das barras, valores que vão dimensionar as mesmas, no nosso caso o array de renda média;
            color: Um argumento opicional que determina a cor das barras.'''

#Fazendo o gráfico para os produtos energéticos e não energéticos
barWidth = 0.4
plt.figure(figsize = (10, 5))
r1 = np.arange(len(energetico_total.iloc[:, 1]))
r2 = [x + barWidth for x in r1]
plt.bar(r1, energetico_total.iloc[:, 0], color = '#4169E1', width = barWidth, label = 'Energético')
plt.bar(r2, nao_energetico_total.iloc[:, 0], color = '#1E90FF', width = barWidth, label = 'Não Energético')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(energetico_total.iloc[:, 0]))], energetico_total['Ano'])
plt.ylabel('Total Produção Anual (10^8 m³)')
plt.title('Produção de produtos energéticos e não energéticos derivados do petróleo (2009 - 2018)')
plt.legend()
plt.show() 

'''Explicando os parâmetros para plotar o gráfico:
   barwidth - dimensiona o tamanho da largura das barras.
   plt.figure(figsize) - aumenta o gráfico para termos uma melhor visualização dos dados.
   r1, r2 - Com estas variáveis é possível ter uma barra do lado da outra, primeiramente
   é checada a largura da primeira barra e depois de forma incremental se posicionam as 
   outras, pela referência das larguras das anteriores.
   Com este método que é construída a barra, com diferencial que adicionamos as variáveis
   que representam as posições (r1,r2) como argumento, e também a largura das barras (barWidth).
   xticks() - Embora já termos o utilizado para adicionar labels no eixo X, neste tipo de gráfico
   há uma particularidade, há um for loop que distribui as legendas uniformemente em cada um dos grupos.
   title() -  Adiciona o título do gráfico.
   legend() - Cria uma legenda para o gráfico.
   show() - Por fim, show mostra o gráfico na tela.'''       