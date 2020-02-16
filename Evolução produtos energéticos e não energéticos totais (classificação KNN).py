import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

'''Aqui vamos usar um método de classificação usando o KNN, para saber como o computador irá dizer qual o tipo de produto derivado do petróleo. '''

dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

#Criação de uma variável com variáveis independentes(x)
previsores = dados.iloc[:, [0, 3]].values

#Criação de uma variável com variável de resposta(y)
classe = dados.iloc[:, 1].values

#Aqui iremos transformar as colunas categóricas em colunas numéricas
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])

#Aqui hávera a divisão dos dados para treinamento e teste passando como parâmetros(variavel independente, variável resposta, a amostra de teste[0 até 1] e divisao da base de dados igual)
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.3, random_state = 0)

'''Agora vamos treinar o algoritmo knn, ajustando o número de vizinhos e usar a base de treinamento para treinar o modelo
   sobre o n_neighbors(número de vizinhos) o valor é ajustado de acordo com a sua vontade. Os valores mais utilizados são 3 ou 5. '''

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

'''Obs: Como constatado, a taxa de acerto do modelo foi 69%, aproximadamente, com 30% de dados para teste.'''
