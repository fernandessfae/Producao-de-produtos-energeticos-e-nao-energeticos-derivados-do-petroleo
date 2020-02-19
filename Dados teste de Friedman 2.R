#Obs: Para realizar o teste de Friedman e Nemenyi, é necessário ter o R versão 3.5.0 instalado. 

#install.packages("devtools")
#devtools::install_github("trnnick/TStools")
require(TStools)

#Carregamento e visualização dos dados de precisão/resultados dos modelos de machine learning
dados = read.csv(file.choose(), encoding= 'UTF-8',check.names = FALSE, sep = ',')
View(dados)

#Visualização da matriz dos dados de precisão/resultados dos modelos de machine learning
matriz <- as.matrix(dados)

#Remoção da coluna sem o modelo treinado
matriz <- matriz[, -4]

#Aplicação do teste estatístico de Friedman e Nemenyi
tsutils::nemenyi(matriz,conf.level = 0.95,plottype="vline")