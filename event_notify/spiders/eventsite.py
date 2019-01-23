import os
from urllib.parse import urljoin
import scrapy


class EventsiteSpider(scrapy.Spider):
    name = "eventsite"
    allowed_domains = [os.getenv("ALLOWED_DOMAINS")]
    start_urls = [os.getenv("START_URLS")]
    root_url = os.getenv("ROOT_URL")

    def parse(self, response):
        for url in response.css(
            "header.c-eventSummary-header > a::attr('href')"
        ).extract():
            yield scrapy.Request(urljoin(self.root_url, url), self.parse_event)

    def parse_event(self, response):
        pass
