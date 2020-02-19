import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

'''Nessa etapa, iremos salvar os melhores classificadores para a identificação
dos produtos energéticos e não energéticos '''

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

#Criação dos melhores algoritmos classificadores
classificador_knn = KNeighborsClassifier(n_neighbors = 3)
classificador_knn.fit(previsores, classe)

classificador_tree = DecisionTreeClassifier()
classificador_tree.fit(previsores, classe)

classificador_forest = RandomForestClassifier(criterion = 'gini', random_state = 0)
classificador_forest.fit(previsores, classe)

#Salvar os classificadores criados
import pickle
pickle.dump(classificador_knn, open('naive_knn2.sav', 'wb'))
pickle.dump(classificador_tree, open('naive_tree2.sav', 'wb'))
pickle.dump(classificador_forest, open('naive_forest2.sav', 'wb'))