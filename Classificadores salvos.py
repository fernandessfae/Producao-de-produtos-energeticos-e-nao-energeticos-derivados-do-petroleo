import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

'''Nessa etapa, iremos salvar os melhores classificadores para a identificação dos produtos derivados de petróleo '''

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

#Criação dos melhores algoritmos classificadores
classificador_naive = GaussianNB()
classificador_naive.fit(previsores, classe)

classificador_tree = DecisionTreeClassifier()
classificador_tree.fit(previsores, classe)

#Salvar os classificadores criados
import pickle
pickle.dump(classificador_naive, open('naive_salvo.sav', 'wb'))
pickle.dump(classificador_tree, open('tree_salvo.sav', 'wb'))
 
