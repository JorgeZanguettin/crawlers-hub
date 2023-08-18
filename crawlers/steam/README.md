# **Steam**

## O que é Steam?

Steam é um software de gestão de direitos digitais criado pela Valve Corporation ou Valve L.L.C., de plataformas digitais como jogos e aplicativos de programação e fornece serviços facilitados como atualização automática de jogos, e preços acessíveis aos usuários.

## **Dados Coletados**

## Variaveis

```yaml
{
name : String,
url : String,
release_date : String,
review_summary : String,
start_price : Float,
discount_pct : Int,
final_price : Float
}
```

## Amostra

| name | url | release_date | review_summary | start_price | discount_pct | final_price |
|---|---|---|---|---|---|---|
| Forza Horizon 5 | https://store.steampowered.com/app/1551360/Forza_Horizon_5/ | 8 Nov, 2021 | Very Positive.88% of the 122,978 user reviews for this game are positive. | 59,99€ | -50% | 29,99€ |
| The Texas Chain Saw Massacre | https://store.steampowered.com/app/1433140/The_Texas_Chain_Saw_Massacre/ | 18 Aug, 2023 | ; | 38,99€ | -10% | 35,09€ |
| Cyberpunk 2077 | https://store.steampowered.com/app/1091500/Cyberpunk_2077/ | 9 Dec, 2020 | Very Positive.80% of the 552,029 user reviews for this game are positive...This product has experienced one or more periods of off-topic review activity.  Based on your preferences, the reviews within these periods have been excluded from this product's Review Score. | 59,99€ | -50% | 29,99€ |
| Shadow Gambit: The Cursed Crew | https://store.steampowered.com/app/1545560/Shadow_Gambit_The_Cursed_Crew/ | 17 Aug, 2023 | Very Positive.98% of the 190 user reviews for this game are positive. | 39,99€ | -10% | 35,99€ |
| BOOK OF HOURS | https://store.steampowered.com/app/1028310/BOOK_OF_HOURS/ | 17 Aug, 2023 | Very Positive.97% of the 244 user reviews for this game are positive. | 24,50€ | -10% | 22,05€ |


## Como executar?

1. Faça o download e instalação do Python 3 [Aqui](https://www.python.org/).
2. Direcione o seu bash de preferencia a pasta raiz do repositorio e instale as dependencias utilizando o comando ```pip install -r requirements.txt``` ou ```pip3 install -r requirements.txt``` .
3. Execute o Crawler com o comando ```python steam.py``` ou ```python3 steam.py``` .
4. Pronto! Os dados coletados serão armazenados em um arquivo CSV na raiz do projeto com o nome **games.csv**.
