import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from yellowbrick.classifier import ConfusionMatrix

'''Aqui vamos usar um método de classificação usando a Árvore de Decisão, para saber como o computador irá dizer qual o tipo de produto derivado do petróleo. '''

dados = pd.read_csv('Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';', decimal = ',')

#Criação de uma variável com variáveis independentes(x)
previsores = dados.iloc[:, [0, 3]].values

#Criação de uma variável com variável de resposta(y)
classe = dados.iloc[:, 1].values

#Aqui iremos transformar as colunas categóricas em colunas numéricas
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])

#Aqui hávera a divisão dos dados para treinamento e teste 
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.3, random_state = 0)

#Criação do algoritmo da árvore de decisão, juntamente com o treinamento do algoritmo
arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento, y_treinamento)

#Gera um arquivo de texto no diretório específico onde o código está salvo, copia o texto que foi gerado e cola na aba lá presente no site webgraphviz.com para gerar a árvore.
export_graphviz(arvore, out_file = 'tree.dot')

#Faz as previsões da variável teste.
previsoes = arvore.predict(X_teste)

#Gera uma variável com a matriz de confusão
confusao = confusion_matrix(y_teste, previsoes)

#Gera duas variáveis com as taxas de acertos e erros da árvore de decisão
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

#Gera o imagem da matriz de confusão
v = ConfusionMatrix(arvore)
v.fit(X_treinamento, y_treinamento)
v.score(X_teste, y_teste)
v.poof()

'''Obs: Como constatado, a taxa de acerto foi 80%, aproximadamente, com 30% de dados para teste.'''
