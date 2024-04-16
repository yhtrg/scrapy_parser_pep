import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import NAME_SPIDER, URL


class PepSpider(scrapy.Spider):
    name = NAME_SPIDER
    allowed_domains = [URL]
    start_urls = [f'https://{URL}/']

    def parse(self, response):
        for pep in response.css('section#numerical-index tr a::attr(href)'):
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css('h1.page-title::text').get().split(' ')[1],
            'name': ''.join(response.css('h1.page-title::text').get()).strip(),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
