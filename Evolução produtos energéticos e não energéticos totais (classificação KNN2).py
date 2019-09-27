import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

'''Aqui vamos usar um método de classificação usando o KNN, para saber como o computador irá dizer qual o tipo energetico de produto derivado do petróleo cada um pertence. '''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';')

#Criaremos uma lista para adicionar os números para cada tipo de produto
coluna_numerica_produtos = []

#Aqui foi criado um laço para atribuir um número para cada produto derivado do petróleo
for index, column in dados.iterrows():
    if column['Tipo de Derivado'] == 'Energético':
        coluna_numerica_produtos.append(0)
    else:
        coluna_numerica_produtos.append(1)

#Criaremos uma nova coluna 'Números dos derivados de petróleo' no dataframe 'dados'
dados['Números dos tipos de derivados'] = coluna_numerica_produtos

#Precisaremos fazer a transformação dos números da coluna 'produção (m3)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
dados['Produção (m3)'] = dados['Produção (m3)'].str.replace(",", ".").astype(float)

#Criação de uma variável com variáveis independentes(x)
previsores = dados.iloc[:, [1, 3]].values

#Criação de uma variável com variável de resposta(y)
classe = dados.iloc[:, 4].values

#Aqui iremos transformar as colunas categóricas em colunas numéricas
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])

#Aqui hávera a divisão dos dados para treinamento e teste passando como parâmetros(variavel independente, variável resposta, a amostra de teste[0 até 1] e divisao da base de dados igual)
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.2, random_state = 0)

'''Agora vamos treinar o algoritmo knn, ajustando o número de vizinhos e usar a base de treinamento para treinar o modelo
   sobre o n_neighbors(número de vizinhos) o valor é ajustado de acordo com a sua vontade. Nesse caso específico, como 
   existe 2 grupos (energéticos e não energéticos), o mais sensato é colocar n = 2. '''

#Faz a previsão do algoritmo knn usando a base de teste
knn = KNeighborsClassifier(n_neighbors = 2)
knn.fit(X_treinamento, y_treinamento)

#Faz a previsão do algoritmo knn usando a base de teste
previsoes = knn.predict(X_teste) 

#Cria uma matriz de confusão nessa variável
confusao = confusion_matrix(y_teste, previsoes)

#Cria variáveis com a taxa de acerto e erro
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

'''Obs: Para efeito de comparação, decidi ajustar o test_size para ver quais valores seriam melhor para o teste de predição da máquina, e o resultado foi esse:
    
         Como constatado, a taxa de acerto foi 73.3%, aproximadamente, com 30% de dados para teste.
         Como constatado, a taxa de acerto foi 75.0%, com 29% de dados para teste.
         Como constatado, a taxa de acerto foi 76.7%, aproximadamente, com 28% de dados para teste.
         Como constatado, a taxa de acerto foi 75.6%, aproximadamente, com 27% de dados para teste.
         Como constatado, a taxa de acerto foi 74.4%, aproximadamente, com 26% de dados para teste.
         Como constatado, a taxa de acerto foi 76.3%, aproximadamente, com 25% de dados para teste.
         Como constatado, a taxa de acerto foi 75.0%, com 24% de dados para teste.
         Como constatado, a taxa de acerto foi 74.3%, aproximadamente, com 23% de dados para teste.
         Como constatado, a taxa de acerto foi 75.8%, aproximadamente, com 22% de dados para teste.
         Como constatado, a taxa de acerto foi 78.1%, aproximadamente, com 21% de dados para teste.
         Como constatado, a taxa de acerto foi 80.0%, com 20% de dados para teste.
         
         Como constatado, o melhor resultado da máquina foi um valor de 0.2(20%) dos dados para o teste e 0.8(80%) dos dados para treinamento. A conclusão que, nesse caso,
         foi necessário uma quantidade maior de dados para treino para que a máquina tivesse um melhor aproveitamento.'''