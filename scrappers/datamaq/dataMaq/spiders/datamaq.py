import scrapy
import urllib.parse
from ..items import DatamaqItem

class DatamaqSpider(scrapy.Spider):
    name = 'datamaq'
    allowed_domains = []
    custom_settings = {
        'ITEM_PIPELINES': {
            'dataMaq.pipelines.DatamaqPipeline': 400
        },
        "DOWNLOADER_MIDDLEWARES": {
            "dataMaq.middlewares.DatamaqSpiderMiddleware": 400,
            "dataMaq.middlewares.ScrapyTelegramBotMiddleware": 405
        }
    }

    start_urls = [
        'http://www.datamaq.org.br/SearchResult/AdditionalFilter?parentId=undefined&sectorName=undefined&isSegment=undefined'
    ]

    def parse(self, response):
        replace_characters = [
            ("showChildSector('", ""),
            ("');", ""),
            ("', '", ","),
        ]

        for obj_url in response.css('input.btn.btn-outline-info::attr(onclick)').extract():
            if 'showChildSector' in str(obj_url):
                obj_child = obj_url
                for r in replace_characters:
                    obj_child = obj_child.replace(
                        r[0], r[1]
                    )
                obj_child = obj_child.split(",")

                id_categoria = obj_child[0]
                categoria = obj_child[1]

                url_categoria = 'http://www.datamaq.org.br/SearchResult/AccountIndustrialSectorList?industrialSectorId={}&sectorName={}&isSegment=undefined'.format(
                    id_categoria,
                    urllib.parse.quote_plus(categoria)
                )

                yield scrapy.Request(
                    url=url_categoria,
                    callback=self.parse_category
                )

    def parse_category(self, response):
        for empresa_block in response.css("table.table.table-sm.table-hover tbody tr::attr(onclick)").extract()[0:1]:
            yield scrapy.Request(
                url=self.get_url_companies(empresa_block),
                callback=self.parse_company_details,
                dont_filter=True
            )

    def parse_company_details(self, response):
        replace_characters = [
            ":",
            "º",
            " ",
            "-"
        ]

        self.item_empresa = DatamaqItem()
        
        self.item_empresa['UrlEmpresa'] = response.url
        for block_prop in response.css("div.container div.row"):
            field_name = block_prop.css("div.col-2 span::text").extract_first()

            if not field_name:
                continue

            for r in replace_characters:
                field_name = field_name.replace(
                    r[0], ""
                )

            field_value = block_prop.css("div.col span::text").extract_first()

            if field_value:
                field_value = str(field_value).strip()
            else:
                field_value = block_prop.css("div.col a::text").extract_first()

                if field_value:
                    field_value = str(field_value).strip()
                else:
                    continue

            self.item_empresa[field_name] = field_value

        yield scrapy.Request(
            url=self.get_url_products(
                response.xpath('/html/body/div[3]/div[1]/input/@onclick').extract_first()
            ),
            callback=self.parse_product_details,
            dont_filter=True
        )

    def parse_product_details(self, response):
        self.item_empresa['Produtos'] = response.css('table.table.table-sm.table-hover tbody tr td a::text').extract()

        yield self.item_empresa

    @staticmethod
    def get_url_products(empresa_block):
        propriedades = str(empresa_block).replace('openLineOfProduction(', '').replace(');', '').replace("'", "").split(', ')

        return 'http://www.datamaq.org.br/SearchResult/LineOfProduction?sectorId={}&sectorName={}&entityId={}&entityIDName={}&isSector={}'.format(
            propriedades[0],
            urllib.parse.quote_plus(propriedades[1]),
            propriedades[2],
            urllib.parse.quote_plus(propriedades[3]),
            propriedades[4],
        )

    @staticmethod
    def get_url_companies(empresa_block):
        propriedades_empresa = str(empresa_block).replace('openAccountDetail(', '').replace(');', '').replace("'", "").split(', ')

        return 'http://www.datamaq.org.br/SearchResult/ShowManufacturer?sectorId={}&sectorName={}&entityId={}&entityIDName={}&sourceType=2&industrialInstallationProductId=&isSector=1'.format(
            propriedades_empresa[0],
            urllib.parse.quote_plus(propriedades_empresa[1]),
            propriedades_empresa[2],
            urllib.parse.quote_plus(propriedades_empresa[3]),
        )
