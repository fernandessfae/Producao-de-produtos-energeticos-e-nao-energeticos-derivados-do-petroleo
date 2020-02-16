import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

'''Aqui vamos usar um método de classificação usando a Regressão Logística, para saber como o computador irá dizer qual o tipo energético de cada produto derivado do petróleo. '''

dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

#Criação de uma variável com variáveis independentes(x)
previsores = dados.iloc[:, [1, 3]].values

#Criação de uma variável com variável de resposta(y)
classe = dados.iloc[:, 0].values

#Aqui iremos transformar as colunas categóricas em colunas numéricas
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])

#Fazendo a padronização dos atributos previsores
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

#Aqui hávera a divisão dos dados para treinamento e teste
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.3, random_state = 0)

#Criação e treinamento do regressor logístico
regressor_logistico = LogisticRegression(solver = 'liblinear')
regressor_logistico.fit(X_treinamento, y_treinamento)

#Previsões com o algoritmo criado
previsoes = regressor_logistico.predict(X_teste)

#Medição da acurácia do modelo e sua matriz de confusão
precisao = accuracy_score(y_teste, previsoes)
matriz = confusion_matrix(y_teste, previsoes)

#Visualização da matriz de confusão
v = ConfusionMatrix(regressor_logistico)
v.fit(X_treinamento, y_treinamento)
v.score(X_teste, y_teste)
v.poof()

'''Obs: Como constatado, a taxa de acerto do modelo foi 64.4%, aproximadamente, com 30% de dados para teste.'''
