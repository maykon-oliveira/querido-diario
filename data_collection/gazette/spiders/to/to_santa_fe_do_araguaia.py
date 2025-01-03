from datetime import date

from gazette.spiders.base.diariooficialbr import BaseDiarioOficialBRSpider


class ToSantaFedoAraguaiaSpider(BaseDiarioOficialBRSpider):
    TERRITORY_ID = "1718865"
    name = "to_santa_fe_do_araguaia"
    allowed_domains = ["santafedoaraguaia.diariooficialbr.com.br"]
    BASE_URL = "https://santafedoaraguaia.diariooficialbr.com.br"
    start_date = date(2021, 2, 5)
