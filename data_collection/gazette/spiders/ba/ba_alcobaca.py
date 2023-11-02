from datetime import date

from gazette.spiders.base.doem import DoemGazetteSpider


class BaAlcobacaSpider(DoemGazetteSpider):
    TERRITORY_ID = "2900801"
    name = "ba_alcobaca"
    state_city_url_part = "ba/alcobaca"
    start_date = date(2017, 3, 3)
