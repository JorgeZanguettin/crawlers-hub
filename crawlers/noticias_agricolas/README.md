# **Noticias Agricolas**

## O que é Noticias Agricolas?

Fundado em 1997, o site Notícias Agrícolas é, atualmente, um dos mais importantes meios de comunicação do agronegócio brasileiro. O portal preza pela comunicação direta com os produtores rurais e cria um espaço com ampla diversidade de opiniões e informações em tempo real, com conteúdo de qualidade para que nossos usuários possam tomar sempre as melhores decisões.

## **Dados Coletados**

## Variaveis

```yaml
{
titulo : String,
noticia : String,
url : String,
data : Datetime
}
```

## Amostra

| TITULO | NOTICIA | URL | DATA | 
| --- | --- | --- | --- | 
|Petróleo Brent sobe e se aproxima de US$ 50 com expectativa por estímulo nos EUA | ..NOVA YORK (Reuters) - Os contratos futuros do petróleo Brent avançaram mais de 1% nesta sexta-feira, permanecendo pouco abaixo da marca de 50 dólares por barril, à medida que expectativas de um pacote de estímulos econômicos nos Estados Unidos... | https://www.noticiasagricolas.com.br/noticias/petroleo/275399-petroleo-brent-sobe-e-se-aproxima-de-us-50-com-expectativa-por-estimulo-nos-eua.html | 05/12/2020 09:34 |
|Na reta final, plantio de soja avança pouco em MT na semana | ..SÃO PAULO (Reuters) - O plantio de soja 2020/21 registrou um ligeiro avanço de 0,27 ponto percentual na última semana, para 99,92% da área estimada em Mato Grosso... | https://www.noticiasagricolas.com.br/noticias/soja/275397-na-reta-final-plantio-de-soja-avanca-pouco-em-mt-na-semana.html | 04/12/2020 21:42 |
|Exportador de café Terra Forte tem plano de recuperação judicial homologado | ..SÃO PAULO (Reuters) - O conglomerados exportador de café Terra Forte teve seu plano de recuperação judicial homologado na Corte de Campinas (SP)... | https://www.noticiasagricolas.com.br/noticias/cafe/275396-exportador-de-cafe-terra-forte-tem-plano-de-recuperacao-judicial-homologado.html | 04/12/2020 21:41 |
|Mourão diz que governo poderia ter orientado melhor sobre isolamento, mas aponta "paixonite" política | No momento em que o presidente julgar necessário ele vai estabelecer as ligações, que eu acredito que, por via da nossa embaixada em Washington, já estão sendo feitas... | https://www.noticiasagricolas.com.br/noticias/politica-economia/275394-mourao-diz-que-governo-poderia-ter-orientado-melhor-sobre-isolamento-mas-aponta-paixonite-politica.html | 04/12/2020 19:09 |

## Como executar?

1. Faça o download e instalação do Python 3 [Aqui](https://www.python.org/).
2. Direcione o seu bash de preferencia a pasta raiz do repositorio e instale as dependencias utilizando o comando ```pip install -r requirements.txt``` ou ```pip3 install -r requirements.txt``` .
3. Execute o Crawler com o comando ```python noticias_agricolas.py``` ou ```python3 noticias_agricolas.py``` .
4. Pronto! Os dados coletados serão armazenados em um arquivo CSV na raiz do projeto com o nome **noticias.csv**.