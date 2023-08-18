# **Idealista**

## O que é Idealista?

Tem como missão é fornecer informação imobiliária estruturada e organizada de forma homogénea e em tempo real, ao alcance de qualquer profissional do setor. Dispondo de um conjunto de ferramentas tecnológicas e analíticas para processar, padronizar e estruturar fontes de dados úteis e convertê-las em informação facilmente acessível.

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
| Apartamento T0 na rua Giovanni Antinori, 2, Rio Seco - Casalinho, Ajuda | https://www.idealista.pt/imovel/31052742/ | 900€/mês | T0 | 55 m² área bruta | MARAVILHOSO ESTÚDIO COMO NOVO localizado ao pé... |
| Apartamento T2, Calçada da Ajuda, Calçada da Ajuda - Belém, Ajuda | https://www.idealista.pt/imovel/32831581/ | 2.950€/mês | T2 | 94 m² área bruta | "Apartamento T2 inserido, inserido no prestigiado... |
| Apartamento T2 em Boa Hora, Ajuda | https://www.idealista.pt/imovel/32644962/ | 1.600€/mês | T2 | 78 m² área bruta | Venha conhecer este excelente T2+1, acabado de remodelar e pronto a estrear... |
| Duplex, Calçada do Mirante, Alto da Ajuda, Ajuda | https://www.idealista.pt/imovel/32774575/ | 1.890€/mês | T2 | 130 m² área bruta | T2 duplex mobilado, com vista para o Palácio da Ajuda e o Tejo... |
| Apartamento T4 em Boa Hora, Ajuda | https://www.idealista.pt/imovel/32582590/ | 3.700€/mês | T4 | 170 m² área bruta | Apartamento com vista maravilhosa sobre o rio... |


## Como executar?

1. Faça o download e instalação do Python 3 [Aqui](https://www.python.org/).
2. Direcione o seu bash de preferencia a pasta raiz do repositorio e instale as dependencias utilizando o comando ```pip install -r requirements.txt``` ou ```pip3 install -r requirements.txt``` .
3. Execute o Crawler com o comando ```python idealista.py``` ou ```python3 idealista.py``` .
4. Pronto! Os dados coletados serão armazenados em um arquivo CSV na raiz do projeto com o nome **imoveis.csv**.
