# **OLX**

## O que é OLX?

OLX Portugal: Compre e venda anúncios de carros, motas, casas, apartamentos, telemóveis, tablets, animais, sofás, móveis e todo o tipo de produtos de moda e acessórios. Tudo ao melhor preço em Portugal.

## **Dados Coletados**

## Variaveis

```yaml
{
title : String,
url : String,
price : Float,
}
```

## Amostra

| title | url | price |
|---|---|---|
| Arrenda-se apartamento | https://www.olx.com/d/anuncio/arrenda-se-apartamento-IDHSqEj.html | 850 € |
| Fabuloso apartamento T1 em condomínio de Luxo Laranjeiras | https://www.olx.com/d/anuncio/fabuloso-apartamento-t1-em-condomnio-de-luxo-laranjeiras-IDHQGWc.html | 1.700 € |
| Alugo T2 terraços do rio coimbra | https://www.olx.com/d/anuncio/alugo-t2-terraos-do-rio-coimbra-IDHSNkv.html | 950 € |
| Apartamento T2 - Jardins da Parede. | https://www.imovirtual.com/pt/anuncio/apartamento-t2-jardins-da-parede-ID1bAi2.html | 1.950 € |
| Alugo Apartamento T1 | https://www.olx.com/d/anuncio/alugo-apartamento-t1-IDHSISF.html | 1.100 € |


## Como executar?

1. Faça o download e instalação do Python 3 [Aqui](https://www.python.org/).
2. Direcione o seu bash de preferencia a pasta raiz do repositorio e instale as dependencias utilizando o comando ```pip install -r requirements.txt``` ou ```pip3 install -r requirements.txt``` .
3. Execute o Crawler com o comando ```python olx.py``` ou ```python3 olx.py``` .
4. Pronto! Os dados coletados serão armazenados em um arquivo CSV na raiz do projeto com o nome **imoveis.csv**.
