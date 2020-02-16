import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from sklearn.neural_network import MLPClassifier

'''Aqui vamos usar um método de classificação usando a Redes Neurais (MLP), para saber como o computador irá dizer qual o tipo de produto derivado do petróleo. '''

dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

#Criação de uma variável com variáveis independentes(x)
previsores = dados.iloc[:, [0, 3]].values

#Criação de uma variável com variável de resposta(y)
classe = dados.iloc[:, 1].values

#Aqui iremos transformar as colunas categóricas em colunas numéricas
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])

#Fazendo a padronização dos atributos previsores
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

#Aqui hávera a divisão dos dados para treinamento e teste 
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.3, random_state = 0)

#Criação e treinamento da rede neural 
rede = MLPClassifier(hidden_layer_sizes = (200,), max_iter = 3000, tol = 0.0000010, verbose = True)
rede.fit(X_treinamento, y_treinamento)

#Faz as previsões da variável teste.
previsoes = rede.predict(X_teste)

#Gera uma variável com a matriz de confusão
confusao = confusion_matrix(y_teste, previsoes)

#Gera duas variáveis com as taxas de acertos e erros da árvore de decisão
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

#Gera o imagem da matriz de confusão
v = ConfusionMatrix(rede)
v.fit(X_treinamento, y_treinamento)
v.score(X_teste, y_teste)
v.poof()

'''Obs: Como constatado, a taxa de acerto do modelo foi 84.4%, aproximadamente, com 30% de dados para teste.'''