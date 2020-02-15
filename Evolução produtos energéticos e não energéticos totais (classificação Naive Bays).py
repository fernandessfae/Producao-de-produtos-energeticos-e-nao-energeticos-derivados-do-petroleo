import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix, accuracy_score
from yellowbrick.classifier import ConfusionMatrix

'''Aqui vamos usar um método de classificação usando o Naive Bays, para saber como o computador irá dizer qual o tipo de produto derivado do petróleo. '''

dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')  
     
#Criação de uma variável com variáveis independentes(x)
previsores = dados.iloc[:, [0, 3]].values

#Criação de uma variável com variável de resposta(y)
classe = dados.iloc[:, 1].values

#Aqui iremos transformar as colunas categóricas em colunas numéricas
onehotencoder = ColumnTransformer(transformers = [('OneHotEncoder', OneHotEncoder(), [0])], remainder = 'passthrough')
previsores = onehotencoder.fit_transform(previsores)

#Aqui hávera a divisão dos dados para treinamento e teste 
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.3, random_state = 0)

#Agora vamos aplicar o naive bays nos dados de treinamento
naive_bayes = GaussianNB()
naive_bayes.fit(X_treinamento, y_treinamento)

#Pega os dados passados no passo anterior para ser executado no modelo
previsoes = naive_bayes.predict(X_teste)

#gera uma variável com uma matriz de confusão
confusao = confusion_matrix(y_teste, previsoes)

#Revela o percentual de acerto e erro do modelo da máquina
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

#Aqui irá gerá a figura da matriz de confusão (executar os 4 comandos simultaneamente)
v = ConfusionMatrix(naive_bayes)
v.fit(X_treinamento, y_treinamento)
v.score(X_teste, y_teste)
v.poof()

'''Como constatado, a taxa de acerto do modelo foi 66.7%, aproximadamente, com 30% de dados para teste.'''
