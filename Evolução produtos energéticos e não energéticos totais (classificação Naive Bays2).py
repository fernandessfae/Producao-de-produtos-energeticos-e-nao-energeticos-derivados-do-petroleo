import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from yellowbrick.classifier import ConfusionMatrix

'''Aqui vamos usar um método de classificação usando o Naive Bays, para saber como o computador irá dizer qual o tipo de derivado do petróleo cada produto pertence. '''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Distribuição percentual da produção de derivados de petróleo não energéticos.csv', sep = ';')

#Criaremos uma lista para adicionar os números para cada tipo de produto derivado do petróleo
coluna_numerica_produtos = []

#Aqui foi criado um laço para atribuir um número para cada tipo  do produto derivado do petróleo
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
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.25, random_state = 0)

#Agora vamos aplicar o naive bays nos dados de treinamento (executa os dois comandos simultaneamente)
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
v = ConfusionMatrix(GaussianNB())
v.fit(X_treinamento, y_treinamento)
v.score(X_teste, y_teste)
v.poof()

'''Obs: Para efeito de comparação, decidi ajustar o test_size para ver quais valores seriam melhor para o teste de predição da máquina, e o resultado foi esse:
    
         Como constatado, a taxa de acerto foi 64.4%, aproximadamente, com 30% de dados para teste.
         Como constatado, a taxa de acerto foi 68.2%, aproximadamente, com 29% de dados para teste.
         Como constatado, a taxa de acerto foi 67.4%, aproximadamente, com 28% de dados para teste.
         Como constatado, a taxa de acerto foi 68.3%, aproximadamente, com 27% de dados para teste.
         Como constatado, a taxa de acerto foi 69.2%, aproximadamente, com 26% de dados para teste.
         Como constatado, a taxa de acerto foi 71.1%, aproximadamente, com 25% de dados para teste.
         Como constatado, a taxa de acerto foi 69.4%, aproximadamente, com 24% de dados para teste.
         Como constatado, a taxa de acerto foi 68.6%, aproximadamente, com 23% de dados para teste.
         Como constatado, a taxa de acerto foi 66.7%, aproximadamente, com 22% de dados para teste.
         Como constatado, a taxa de acerto foi 65.6%, aproximadamente, com 21% de dados para teste.
         Como constatado, a taxa de acerto foi 66.7%, aproximadamente, com 20% de dados para teste.
         
         Como constatado, o melhor resultado da máquina foi um valor de 0.25(25%) dos dados para o teste e 0.75(75%) dos dados para treinamento. A conclusão que se
         tira é de que nem sempre muitos dados para treinamento faz com que o teste seja mais eficiente, e nem de menos. Isso mostra que os dados tem que ser ajustados
         ao ponto máximo da performance dele, nem para mais, nem para menos.'''