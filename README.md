# Google-Trends
Este repositório é um trabalho desenvolvido pelo Grupo A do projeto Covid Data Analytics (veja mais em covid.dcc.ufmg.br). Aqui é desenvolvida a coleta de dados relativos ao Google Trends e o calculo de suas correlações com os indicadores oficiais de Minas Gerais e do Brasil disponíveis na pasta de indicadores epidemiológicos do seguinte repositório do projeto:https://github.com/CDA-EPCWeb/Tratamento-de-dados/tree/master/Indicadores%20Epidemiol%C3%B3gicos/resultados, na forma do arquivo indicadores.db. Além disso, são geradas diferentes visualizações para os dados obtidos.

# Objetivos
O objetivo principal desse repositório é explorar a possibilidade de se prever a progressão dos indicadores oficiais new week cases(novos casos na semana) e new week deaths(novas mortes na semana) a partir do aumento ou a redução das buscas por certos termos no Google, usando, para isso, a correlação de Spearman ou Pearson entre esses dados.

# Pré-requisitos: jupyter
Para conseguir executar os notebooks(arquivos .ipynb) é necessário, primeiramente, fazer o download de Python(disponível em:https://www.python.org/) ou da interface de Python anaconda (disponível em:https://anaconda.org/anaconda/python). Após isso, deve-se instalar a extensão jupyter notebooks, o que pode ser feito das seguintes maneiras:

1-Abra o python powershell ou o anaconda prompt. Digite: pip install jupyterlab

2-Alternativamente, caso tenha escolhido instalar anaconda, pode-se digitar conda install -c conda-forge jupyterlab.

# Pré-requisitos: bibliotecas
Para a execução dos notebooks desse repositório, são necessárias algumas bibliotecas além das padrões de python. Essas são: Pandas, Matplotlib, Sqlite3, numpy, pytrends e wordcloud. Elas podem ser instaladas digitando os seguintes comandos em python powershell ou anaconda prompt:

pip install pandas

pip install matplotlib

pip install numpy

pip install pysqlite3

pip install pytrends

pip install wordcloud

# Bases de dados
A base de dados utilizada para os indicadores oficiais é gerada por outro repositório do projeto CDA e está disponíel em: https://github.com/CDA-EPCWeb/Tratamento-de-dados/tree/master/Indicadores%20Epidemiol%C3%B3gicos/resultados. Ela possui 9 indicadores: (novos casos, casos acumulados, novos óbitos, óbitos acumulados, incidencia, letalidade, mortalidade, fator de crescimento e prevalência) para cada, macrorregião, estado, município e para o país como um todo. Porém, para os fins da análise desse repositório só serão usados os novos casos e novos óbitos do Brasil e de Minas Gerais.

Outra base de dados utilizada é a base de dados queries categorizadas, que contém 124 termos relevantes, que foram frequentemente pesquisados, divididos em categorias mais gerais e subcategorias. Essas keywords são aquelas que serão utilizadas para as consultas no Google Trends.

# GtrendsQuery.ipynb
Esse notebook é o responsável pela consulta do Google Trends gerada. Para sua execução é necessária a instalação das bibliotecas pandas, sqlite3, pytrends e numpy, além dos bancos de dados indicadores.db e keywords.csv. A partir disso, o script realizará as consultas relativas às semanas epidemiológicas 9 a 52 e salvará as series temporais resultantes no arquivo SeriesKeywords.csv e SeriesKeywordsMG.csv, que possuem, respectivamente, os dados quanto ao Brasil e Minas Gerais.

# correlacaoAnalise.ipynb
Esse notebook é o responsável por realizar o calculo de correlação e a partir dele gerar diferentes visualizações para os dados, notávelmente, gráficos de linha, scatter plots e wordclouds. Para sua execução são necessárias as bibliotecas pandas, sqlite3, numpy, matplotlib e wordcloud, além dos arquivos gerados por GtrendsQuery.ipynb, indicadores.db e Queries categorizadas.csv. O algoritmo utilizado para os bubblegraphs foi baseado em https://matplotlib.org/devdocs/gallery/misc/packed_bubbles.html

O output do código são os arquivos que podem ser vistos nas diversas pastas desse repositório: as spreadsheets da pasta Correlations, os gráficos da pasta Sintomas, os gráficos da pasta Top10, as wordclouds da pasta Wordclouds e os bubble graphs da pasta Bubbles.

# Metodologia de tratamento
--------------------------------(feito por membros que não estão mais no grupo,preciso procurar com o Evandro)------------------------------------------------------------------

# Resultados
Esse repositório ao fim da execução desses vários notebooks gera não somente as correlações entre os indicadores e as keywords utilizadas, como também diversas visualizações, o que permite uma mais fácil observação de relações entre esses dois dados, que podem ser vistas, por exemplo, por meio de gráficos como os abaixo:

![image](https://user-images.githubusercontent.com/57831311/109388084-af5dc700-78e3-11eb-9070-724626972211.png)

![image](https://user-images.githubusercontent.com/57831311/109388090-b84e9880-78e3-11eb-819a-0cc2189f6747.png)

Outro resultado são imagens de facil interpretação no geral, como os bubble graphs e wordclouds, nos quais o tamanho da bolha e palavra, respectivamente, indica quão alta é a correlação. Exemplos da aplicação desses métodos na pesquisa incluem:
Bubble graph das correlações em relação aos novos casos em MG(azul=positivo, vermelho=negativo):
![image](https://user-images.githubusercontent.com/57831311/109874498-f504f180-7c4d-11eb-9ada-10b535294e38.png)
Wordcloud das correlações em relação aos novos casos em MG a partir de seu valor absoluto:
![image](https://user-images.githubusercontent.com/57831311/109874727-3f866e00-7c4e-11eb-8be9-f8aeb7dbb7bb.png)


