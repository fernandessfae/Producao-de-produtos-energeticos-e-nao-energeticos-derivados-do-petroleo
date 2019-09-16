import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de produtos unicamente energéticos derivados do petróleo entre os anos de 2009 a 2018, e fazer a sua comparação (isolados e juntos).
    Produtos energéticos - Asfalto, Coque, Nafta, Óleo Lubrificante, Parafina, Solvente, Outros.'''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';')

'''Agora faremos a separação dos produtos não energéticos derivados do petróleo.
   1) Faremos a separação dos energéticos e não energéticos usando uma lista para colocarmos num laço.
   2) Iremos ajustar os novos dataframes desmembrado do dataframe inicial
   3) Transformaremos as listas em novos dataframes
   4) Alteração nos nomes das colunas para o mesmo do dataframe inicial'''

# 1º Passo
asfalto = []
coque = []
nafta = []
oleo_lubrificante = []
parafina = []
solvente = []
outros = []

# 2º Passo
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

# 3º Passo
asfalto = pd.DataFrame(list(asfalto))
coque = pd.DataFrame(list(coque))
nafta = pd.DataFrame(list(nafta))
oleo_lubrificante = pd.DataFrame(list(oleo_lubrificante))
parafina = pd.DataFrame(list(parafina))
solvente = pd.DataFrame(list(solvente))
outros = pd.DataFrame(list(outros))

# 4º Passo
asfalto.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
coque.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
nafta.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
oleo_lubrificante.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
parafina.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
solvente.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']
outros.columns = ['Tipo de Derivado', 'Derivados de petróleo', 'Ano', 'Produção (m³)']

#Precisaremos fazer a transformação dos números da coluna 'produção (m³)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
asfalto['Produção (m³)'] = asfalto['Produção (m³)'].str.replace(",", ".").astype(float)
coque['Produção (m³)'] = coque['Produção (m³)'].str.replace(",", ".").astype(float)
nafta['Produção (m³)'] = nafta['Produção (m³)'].str.replace(",", ".").astype(float)
oleo_lubrificante['Produção (m³)'] = oleo_lubrificante['Produção (m³)'].str.replace(",", ".").astype(float)
parafina['Produção (m³)'] = parafina['Produção (m³)'].str.replace(",", ".").astype(float)
solvente['Produção (m³)'] = solvente['Produção (m³)'].str.replace(",", ".").astype(float)
outros['Produção (m³)'] = outros['Produção (m³)'].str.replace(",", ".").astype(float)

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

#Plotando o gráfico de outros produtos energéticos
plt.bar(outros.iloc[:, 2], outros.iloc[:, 3], color = 'purple')
plt.xticks(outros['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de outros produtos energéticos (2009 - 2018)')

'''Explicando os parâmetros para explicar os gráficos acima:
    xticks() - Com ele definimos as labels do eixo X, ele precisa de um parâmetro com tipo de array que determine as labels.
    xlabel() e ylabel() - Com estes dois métodos adicionamos as labels do eixo Y e X, respectivamente.
    title() - adiciona o título do gráfico.
    plt.bar() - este método da lib plt, inicia a construsção do gráfico de barra, e aí começamos a passar os argumentos, que em ordem são:
            x: As coordernadas das barras do eixo X, que no nosso caso são as faixas etárias;
            height: A ‘altura’ das barras, valores que vão dimensionar as mesmas, no nosso caso o array de renda média;
            color: Um argumento opicional que determina a cor das barras.'''

#Plotando o gráfico comparando todos os produtos energéticos
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

'''Explicando os parâmetros para plotar o gráfico:
   barwidth - dimensiona o tamanho da largura das barras.
   plt.figure(figsize) - aumenta o gráfico para termos uma melhor visualização dos dados.
   r1, r2, r3, r4, r5, r6, r7 - Com estas variáveis é possível ter uma barra do lado
   da outra, primeiramente é checada a largura da primeira barra e depois de forma incremental
   se posicionam as outras, pela referência das larguras das anteriores.
   bar() - Com este método que é construída a barra, com diferencial que adicionamos as variáveis
   que representam as posições (r1,r2, r3, r4, r5, r6, r7) como argumento, e também a largura das barras (barWidth).
   xticks() - Embora já termos o utilizado para adicionar labels no eixo X, neste tipo de gráfico
   há uma particularidade, há um for loop que distribui as legendas uniformemente em cada um dos grupos.
   title() -  Adiciona o título do gráfico.
   legend() - Cria uma legenda para o gráfico.
   show() - Por fim, show mostra o gráfico na tela.''' 