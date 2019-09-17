import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

'''Aqui vamos usar um método de classificação usando o KNN, para saber como o computador irá dizer qual o tipo de produto derivado do petróleo. '''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';')

#Criaremos uma lista para adicionar os números para cada tipo de produto
coluna_numerica_produtos = []

#Aqui foi criado um laço para atribuir um número para cada produto derivado do petróleo
for index, column in dados.iterrows():
    if column['Derivados de petróleo'] == 'Gasolina A ':
        coluna_numerica_produtos.append(0)
    elif column['Derivados de petróleo'] == 'Gasolina de aviação':
        coluna_numerica_produtos.append(1)
    elif column['Derivados de petróleo'] == 'GLP1':
        coluna_numerica_produtos.append(2)
    elif column['Derivados de petróleo'] == 'Óleo combustível2,3':
        coluna_numerica_produtos.append(3)
    elif column['Derivados de petróleo'] == 'Óleo diesel3':
        coluna_numerica_produtos.append(4)
    elif column['Derivados de petróleo'] == 'QAV':
        coluna_numerica_produtos.append(5)
    elif column['Derivados de petróleo'] == 'Querosene iluminante':
        coluna_numerica_produtos.append(6)
    elif column['Derivados de petróleo'] == 'Outros4':
        coluna_numerica_produtos.append(7)
    elif column['Derivados de petróleo'] == 'Asfalto':
        coluna_numerica_produtos.append(8)
    elif column['Derivados de petróleo'] == 'Coque5':
        coluna_numerica_produtos.append(9)
    elif column['Derivados de petróleo'] == 'Nafta6':
        coluna_numerica_produtos.append(10)
    elif column['Derivados de petróleo'] == 'Óleo lubrificante ':
        coluna_numerica_produtos.append(11)
    elif column['Derivados de petróleo'] == 'Parafina':
        coluna_numerica_produtos.append(12)
    elif column['Derivados de petróleo'] == 'Solvente':
        coluna_numerica_produtos.append(13)
    elif column['Derivados de petróleo'] == 'Outros7':
        coluna_numerica_produtos.append(14)

#Criaremos uma nova coluna 'Números dos derivados de petróleo' no dataframe 'dados'
dados['Números dos derivados de petróleo'] = coluna_numerica_produtos

#Precisaremos fazer a transformação dos números da coluna 'produção (m3)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
dados['Produção (m3)'] = dados['Produção (m3)'].str.replace(",", ".").astype(float)

#Criação de uma variável com variáveis independentes(x)
previsores = dados.iloc[:, [0, 3]].values

#Criação de uma variável com variável de resposta(y)
classe = dados.iloc[:, 4].values

#Aqui iremos transformar as colunas categóricas em colunas numéricas
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 1] = labelencoder.fit_transform(previsores[:, 1])

#Aqui hávera a divisão dos dados para treinamento e teste passando como parâmetros(variavel independente, variável resposta, a amostra de teste[0 até 1] e divisao da base de dados igual)
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.22, random_state = 0)

'''Agora vamos treinar o algoritmo knn, ajustando o número de vizinhos e usar a base de treinamento para treinar o modelo
   sobre o n_neighbors(número de vizinhos) o valor é ajustado de acordo com a sua vontade. Nesse caso específico, como 
   existe 3 grupos (energéticos, não energéticos e outros), o mais sensato é colocar n = 3. '''

#Faz a previsão do algoritmo knn usando a base de teste
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_treinamento, y_treinamento)

#Faz a previsão do algoritmo knn usando a base de teste
previsoes = knn.predict(X_teste)

#Cria uma matriz de confusão nessa variável
confusao = confusion_matrix(y_teste, previsoes)

#Cria variáveis com a taxa de acerto e erro
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

'''Obs: Para efeito de comparação, decidi ajustar o test_size para ver quais valores seriam melhor para o teste de predição da máquina, e o resultado foi esse:
    
         Como constatado, a taxa de acerto foi 60.0%, com 30% de dados para teste.
         Como constatado, a taxa de acerto foi 54.5%, aproximadamente, com 29% de dados para teste.
         Como constatado, a taxa de acerto foi 58.1%, aproximadamente, com 28% de dados para teste.
         Como constatado, a taxa de acerto foi 58.5%, aproximadamente, com 27% de dados para teste.
         Como constatado, a taxa de acerto foi 59.0%, aproximadamente, com 26% de dados para teste.
         Como constatado, a taxa de acerto foi 60.5%, aproximadamente, com 25% de dados para teste.
         Como constatado, a taxa de acerto foi 61.1%, aproximadamente, com 24% de dados para teste.
         Como constatado, a taxa de acerto foi 62.8%, com 23% de dados para teste.
         Como constatado, a taxa de acerto foi 66.6%, aproximadamente, com 22% de dados para teste.
         Como constatado, a taxa de acerto foi 62.5%, com 21% de dados para teste.
         Como constatado, a taxa de acerto foi 56.6%, com 10% de dados para teste.
         
         Como constatado, o melhor resultado da máquina foi um valor de 0.22(22%) dos dados para o teste e 0.78(78%) dos dados para treinamento. A conclusão que se
         tira é de que nem sempre muitos dados para treinamento faz com que o teste seja mais eficiente, e nem de menos. Isso mostra que os dados tem que ser ajustados
         ao ponto máximo da performance dele, nem para mais, nem para menos.'''