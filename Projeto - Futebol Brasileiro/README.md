![Projeto Final da Capacitação](https://github.com/amandaey/Projeto-Final/assets/135295845/f36a5859-8991-48d3-a29d-fc02c6111fe9)

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/> <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white"/> <img src="https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white"/>

> Status: Concluído :heavy_check_mark:

<p align="justify">Análise de dados do futebol brasileiro realizado por membros da FEA.dev para o projeto de capacitação dos bixos que tem como próposito apurar as inúmeras variáveis que influenciam nas probabilidades do resultado de uma partidade de futebol, e principalmente examinar como esses detalhes se revelam através dos dados numéricos sobre campeonatos no Brasil.</p>

## Membros do Projeto
   :soccer: [Amanda Yamasaki](https://github.com/amandaey) 
  
   :soccer: [Gabriel Grub](https://github.com/GabrielGrub) 
   
   :soccer: [Maria Dulce Matos](https://github.com/mariadulcenbm) 
   
   :soccer: [Paulo Sergio](https://github.com/lauposergio) 
   
   :soccer: [Theo Borten](https://github.com/TheoBorten) 

## Tópicos
:soccer: Contextualização

:soccer: Hipóteses

:soccer: Tratamento

:soccer: Insights

:soccer: Conclusão e Análises Futuras

## Campeonatos Analizados
:soccer: Libertadores

:soccer: Copa do Brasil

:soccer: Brasileirão
    
## Contextualização
Ao contrário de loterias numéricas ou jogos com dados (cujos dados são justos), a “loteria esportiva” do futebol não é caracterizada por seus números equiprováveis. No futebol, jogos costumeiramente têm times favoritos e fatores internos e externos não quantificados no cálculo de probabilidades - como o emocional dos jogadores e as condições do ambiente da partida. Levando essa subjetividade em consideração, pode-se dizer que há uma distribuição de probabilidade desigual entre os possíveis resultados. É com este tipo de problema que nos deparamos ao tentar tratar os dados dos principais campeonatos Brasileiros probabilisticamente, e então, realizamos hipóteses para verificar correlações e padrões-ocultos entre dados coletados sobre esses torneios dos últimos anos no Brasil. 

## Hipóteses
Afim de averiguar as correlações e os padrões-ocultos dos dados dos três campeonatos, formulamos três hipóteses que relacionam o horário da partida e a dinâmica do jogo, a tendência consistente de desempenho de um time nos campeonatos citados e o desempenho individual em partidas anteriores e subsequentes.

1. O horário da partida influencia significativamente a dinâmica do jogo, demonstrando uma relação entre o horário de início e a quantidade de gols marcados.
2. Clubes com maiores investimentos em seu elenco costumam elencar entre as melhores posições do campeonato brasileiro (Brasileirão).
3. Um bom desempenho na temporada passada tende a indicar um bom desempenho na próxima temporada.

## Tratamento dos Dados
Nessa etapa importamos as bibliotecas necessárias para nossa análise completa da base de dados, verificamos as informações dos dados da Libertadores, da Copa do Brasil e do Brasileirão e realizamos a limpeza de dados de valores nulos, valores indesejados e outliers.

## Insights
Criação de funções que auxiliaram a análise das hipóteses mensionadas, organização dos dataframes, preparação dos gráficos e a vizualização dos dados por meio de gráficos de barra, de linha e interativos.

## Análise Futura
Explorar mais profundamento os datasets relativos a Copa do Brasil e  Libertadores e explorar novos datasets como [série A](https://basedosdados.org/dataset/c861330e-bca2-474d-9073-bc70744a1b23?table=18835b0d-233e-4857-b454-1fa34a81b4fa/), que é do campeonato brasileiro série A, mais detalhado e com maiores informaçãoes que os dados analisados por nós até então. Portanto, existem outras hipóteses que podem ser verificadas e analizadas sobre o futebol brasileiro.
