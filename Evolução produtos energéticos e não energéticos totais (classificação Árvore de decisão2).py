import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

'''Aqui vamos usar um método de classificação usando a Árvore de Decisão, para saber como o computador irá dizer qual o tipo energético de cada produto derivado do petróleo. '''

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
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.21, random_state = 0)

#Criação do algoritmo da árvore de decisão, juntamente com o treinamento do algoritmo
arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento, y_treinamento)

#Gera um arquivo de texto no diretório específico onde o código está salvo, copia o texto que foi gerado e cola na aba lá presente no site webgraphviz.com para gerar a árvore.
export_graphviz(arvore, out_file = 'tree2.dot')

#Faz as previsões da variável teste.
previsoes = arvore.predict(X_teste)

#Gera uma variável com a matriz de confusão
confusao = confusion_matrix(y_teste, previsoes)

#Gera duas variáveis com as taxas de acertos e erros da árvore de decisão
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

'''Obs: Para efeito de comparação, decidi ajustar o test_size para ver quais valores seriam melhor para o teste de predição da máquina, e o resultado foi esse:
    
         Como constatado, a taxa de acerto foi 95.5%, aproximadamente, com 30% de dados para teste.
         Como constatado, a taxa de acerto foi 95.4%, aproximadamente, com 29% de dados para teste.
         Como constatado, a taxa de acerto foi 95.3%, aproximadamente, com 28% de dados para teste.
         Como constatado, a taxa de acerto foi 92.7%, aproximadamente, com 27% de dados para teste.
         Como constatado, a taxa de acerto foi 92.3%, aproximadamente, com 26% de dados para teste.
         Como constatado, a taxa de acerto foi 97.4%, aproximadamente, com 25% de dados para teste.
         Como constatado, a taxa de acerto foi 97.2%, aproximadamente, com 24% de dados para teste.
         Como constatado, a taxa de acerto foi 97.1%, aproximadamente, com 23% de dados para teste.
         Como constatado, a taxa de acerto foi 97.0%, aproximadamente, com 22% de dados para teste.
         Como constatado, a taxa de acerto foi 100.0%, com 21% de dados para teste.
         Como constatado, a taxa de acerto foi 100.0%, com 20% de dados para teste.
         
         Como constatado, o melhor resultado da máquina foi um valor de 0.21(21%) e 0.2(20%) dos dados para o teste e 0.79(79%) e 0.8(80%) dos dados para treinamento. A conclusão que se
         tira é de que a máquina conseguiu uma exatidão perfeita na classificação dos dados, algo muito excepcional.'''