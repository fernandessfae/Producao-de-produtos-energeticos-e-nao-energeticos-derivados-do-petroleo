import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

''' O objetivo desse código é testar os modelos já treinados para a detecção de
uma acurácia mais precisa, já que as separação de dados para treinamento e teste
podem fazer uma divisão desbalanceada e comprometer o desempenho do modelo e/ou
gerar uma falsa sensação de modelo ideal para aquela resolução de problema.'''

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

#Criação da lista de 30 testes para cada algoritmo
resultados_30_testes_naive = []
resultados_30_testes_tree = []
resultados_30_testes_logistic = []
resultados_30_testes_svm = []
resultados_30_testes_mlp = []
resultados_30_testes_forest = []
resultados_30_testes_knn = []

#Criação do laço para fazer a validação cruzada de cada algoritmo com uma única base de dados.
for i in range(30):
    kfold = StratifiedKFold(n_splits = 10, shuffle = True, random_state = i)
    resultados_1_rodada_naive = []
    resultados_1_rodada_tree = []
    resultados_1_rodada_logistic = []
    resultados_1_rodada_svm = []
    resultados_1_rodada_mlp = []
    resultados_1_rodada_forest = []
    resultados_1_rodada_knn = []

#Separa os dados previsores de forma proporcional em treinamento e teste, de forma aleatoria  
    for indice_treinamento, indice_teste in kfold.split(previsores, np.zeros(shape = (previsores.shape[0], 1))):
        
        classificador_naive = GaussianNB()
        classificador_tree = DecisionTreeClassifier()
        classificador_logistic = LogisticRegression(solver = 'liblinear')
        classificador_svm = SVC(random_state = 1, C = 2.0, gamma = 'auto')
        classificador_mlp = MLPClassifier(hidden_layer_sizes = (100,), max_iter = 1500, tol = 0.00000001, verbose = False)
        classificador_forest = RandomForestClassifier(criterion = 'gini', random_state = 0)
        classificador_knn = KNeighborsClassifier(n_neighbors = 3)
        
        classificador_naive.fit(previsores[indice_treinamento], classe[indice_treinamento])
        classificador_tree.fit(previsores[indice_treinamento], classe[indice_treinamento])
        classificador_logistic.fit(previsores[indice_treinamento], classe[indice_treinamento])
        classificador_svm.fit(previsores[indice_treinamento], classe[indice_treinamento])
        classificador_mlp.fit(previsores[indice_treinamento], classe[indice_treinamento])
        classificador_forest.fit(previsores[indice_treinamento], classe[indice_treinamento])
        classificador_knn.fit(previsores[indice_treinamento], classe[indice_treinamento])
        
        previsoes_naive = classificador_naive.predict(previsores[indice_teste])
        previsoes_tree = classificador_tree.predict(previsores[indice_teste])
        previsoes_logistic = classificador_logistic.predict(previsores[indice_teste])
        previsoes_svm = classificador_svm.predict(previsores[indice_teste])
        previsoes_mlp = classificador_mlp.predict(previsores[indice_teste])
        previsoes_forest = classificador_forest.predict(previsores[indice_teste])
        previsoes_knn = classificador_knn.predict(previsores[indice_teste])
        
        precisao_naive = accuracy_score(classe[indice_teste], previsoes_naive)
        precisao_tree = accuracy_score(classe[indice_teste], previsoes_tree)
        precisao_logistic = accuracy_score(classe[indice_teste], previsoes_logistic)
        precisao_svm = accuracy_score(classe[indice_teste], previsoes_svm)
        precisao_mlp = accuracy_score(classe[indice_teste], previsoes_svm)
        precisao_forest = accuracy_score(classe[indice_teste], previsoes_forest)
        precisao_knn = accuracy_score(classe[indice_teste], previsoes_knn)

        resultados_1_rodada_naive.append(precisao_naive)
        resultados_1_rodada_tree.append(precisao_tree)
        resultados_1_rodada_logistic.append(precisao_logistic)
        resultados_1_rodada_svm.append(precisao_svm)
        resultados_1_rodada_mlp.append(precisao_mlp)
        resultados_1_rodada_forest.append(precisao_forest)
        resultados_1_rodada_knn.append(precisao_knn)
    
    resultados_1_rodada_naive = np.array(resultados_1_rodada_naive)
    resultados_1_rodada_tree = np.array(resultados_1_rodada_tree)
    resultados_1_rodada_logistic = np.array(resultados_1_rodada_logistic)
    resultados_1_rodada_svm = np.array(resultados_1_rodada_svm)
    resultados_1_rodada_mlp = np.array(resultados_1_rodada_mlp)
    resultados_1_rodada_forest = np.array(resultados_1_rodada_forest)
    resultados_1_rodada_knn = np.array(resultados_1_rodada_knn)
    
    media_naive = resultados_1_rodada_naive.mean()
    media_tree = resultados_1_rodada_tree.mean()
    media_logistic = resultados_1_rodada_logistic.mean()
    media_svm = resultados_1_rodada_svm.mean()
    media_mlp = resultados_1_rodada_mlp.mean()
    media_forest = resultados_1_rodada_forest.mean()
    media_knn = resultados_1_rodada_knn.mean()
    
    resultados_30_testes_naive.append(media_naive)
    resultados_30_testes_tree.append(media_tree)
    resultados_30_testes_logistic.append(media_logistic)
    resultados_30_testes_svm.append(media_svm)
    resultados_30_testes_mlp.append(media_mlp)
    resultados_30_testes_forest.append(media_forest)
    resultados_30_testes_knn.append(media_knn)

#Transforma os resultados dos 30 testes em um array    
resultados_30_testes_naive = np.asarray(resultados_30_testes_naive)
resultados_30_testes_tree = np.asarray(resultados_30_testes_tree)
resultados_30_testes_logistic = np.asarray(resultados_30_testes_logistic)
resultados_30_testes_svm = np.asarray(resultados_30_testes_svm)
resultados_30_testes_mlp = np.asarray(resultados_30_testes_mlp)
resultados_30_testes_forest = np.asarray(resultados_30_testes_forest)
resultados_30_testes_knn = np.asarray(resultados_30_testes_knn)

#Imprime os 30 resultados de cada algoritmo de machine learning
for i in range(resultados_30_testes_naive.size):
    print(str(resultados_30_testes_naive[i]).replace('.', ','))

for i in range(resultados_30_testes_tree.size):
    print(str(resultados_30_testes_tree[i]).replace('.', ','))

for i in range(resultados_30_testes_logistic.size):
    print(str(resultados_30_testes_logistic[i]).replace('.', ','))
    
for i in range(resultados_30_testes_svm.size):
    print(str(resultados_30_testes_svm[i]).replace('.', ','))
    
for i in range(resultados_30_testes_mlp.size):
    print(str(resultados_30_testes_mlp[i]).replace('.', ','))

for i in range(resultados_30_testes_forest.size):
    print(str(resultados_30_testes_forest[i]).replace('.', ','))

for i in range(resultados_30_testes_knn.size):
    print(str(resultados_30_testes_forest[i]).replace('.', ','))
    
'''O resultados dos 30 testes de cada modelo serão colocados numa planilha para 
a visualização dos resultados de precisão de cada modelo, e depois fazer o teste
estatistico para a escolha do melhor(es) modelo(s) para produção. '''