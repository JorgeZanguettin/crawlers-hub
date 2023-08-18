# **Sapo**

## O que é Sapo?

O CASASAPO é o portal imobiliário líder em Portugal, com mais de 400 mil imóveis em divulgação e 1.6000.000 visitantes em média por mês.

## **Dados Coletados**

## Variaveis

```yaml
{
title : String,
url : String,
price : Float,
description : String,
}
```

## Amostra

| title | url | price | description |
|---|---|---|---|
| Apartamento T4 | https://casa.sapo.pt/alugar-apartamento-t4-lisboa-parque-das-nacoes-norte-f2a836cc-1f43-11ee-91bc-060000000057.html | 6.800 € | Renovado · 191m² |
| Apartamento T3 | https://casa.sapo.pt/alugar-apartamento-t3-lisboa-lumiar-a13d8727-2643-11ee-82b9-060000000053.html | 1.700 € | Novo · 122m² |
| Apartamento T3 | https://casa.sapo.pt/alugar-apartamento-t3-lisboa-santa-maria-maior-191cf1a9-34fd-11ee-adb9-060000000054.html | 2.100 € | Usado · 115m² |
| Apartamento T3 | https://casa.sapo.pt/alugar-apartamento-t3-lisboa-campolide-b4b413c3-10d8-11ee-adb9-060000000054.html | 1.700 € | Usado · 110m² |
| Apartamento T2 | https://casa.sapo.pt/alugar-apartamento-t2-lisboa-ajuda-f9186ca9-3d52-11ee-a521-060000000056.html | 1.800 € | Usado · 71m² |

## Como executar?

1. Faça o download e instalação do Python 3 [Aqui](https://www.python.org/).
2. Direcione o seu bash de preferencia a pasta raiz do repositorio e instale as dependencias utilizando o comando ```pip install -r requirements.txt``` ou ```pip3 install -r requirements.txt``` .
3. Execute o Crawler com o comando ```python sapo.py``` ou ```python3 sapo.py``` .
4. Pronto! Os dados coletados serão armazenados em um arquivo CSV na raiz do projeto com o nome **imoveis.csv**.
