# **Imovirtual**

## O que é Imovirtual?

O Imovirtual é a porta de entrada para mais de 300.000 imóveis em Portugal. Porque em cada família que cresce, em cada ida para uma nova cidade, na vontade de alcançar horizontes, há uma necessidade de mudança que exige a resposta perfeita. Esta é a morada certa para abraçar todos os momentos da vida.

## **Dados Coletados**

## Variaveis

```yaml
{
title : String,
url : String,
price : Float,
typology : String,
area : String,
description : String,
}
```

## Amostra

| title | url | price | typology | area | description |
|---|---|---|---|---|---|
| Excelente T2 luminoso, com elevador, 1 lugar de parqueamento. | https://www.imovirtual.com/pt/anuncio/excelente-t2-luminoso-com-elevador-1-lugar-de-parqueamento-ID1bMSd.html#3a014afb4e | 255 000 € /mês | T2 | 75 m² | Apartamento para arrendar: Casal de Cambra, Sintra, Lisboa |
| Apartamento T1 para arrendamento | https://www.imovirtual.com/pt/anuncio/apartamento-t1-para-arrendamento-ID1bRpC.html#3a014afb4e | 900 € /mês | T1 | 79,75 m² | Apartamento para arrendar: Cacém e São Marcos, Sintra, Lisboa |
| Apartamento T3 para arrendamento | https://www.imovirtual.com/pt/anuncio/apartamento-t3-para-arrendamento-ID1bMKm.html#3a014afb4e | 1 100 € /mês | T3 | 81 m² | Apartamento para arrendar: Cacém e São Marcos, Sintra, Lisboa |
| T2 totalmente remodelado em Monte Abraão, Sintra. Cozinha... | https://www.imovirtual.com/pt/anuncio/t2-totalmente-remodelado-em-monte-abraao-sintra-cozinha-ID1bLfe.html#3a014afb4e | 1 150 € /mês | T2 | 60 m² | Apartamento para arrendar: Massamá e Monte Abraão, Sintra, Lisboa |
| Apartamento T3 para arrendamento | https://www.imovirtual.com/pt/anuncio/apartamento-t3-para-arrendamento-ID1bxNj.html#3a014afb4e | 1 250 € /mês | T3 | 132 m² | Apartamento para arrendar: Agualva e Mira-Sintra, Sintra, Lisboa |


## Como executar?

1. Faça o download e instalação do Python 3 [Aqui](https://www.python.org/).
2. Direcione o seu bash de preferencia a pasta raiz do repositorio e instale as dependencias utilizando o comando ```pip install -r requirements.txt``` ou ```pip3 install -r requirements.txt``` .
3. Execute o Crawler com o comando ```python imovirtual.py``` ou ```python3 imovirtual.py``` .
4. Pronto! Os dados coletados serão armazenados em um arquivo CSV na raiz do projeto com o nome **imoveis.csv**.
