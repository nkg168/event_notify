import os
import scrapy


class EventsiteSpider(scrapy.Spider):
    name = "eventsite"
    allowed_domains = [os.getenv("ALLOWED_DOMAINS")]
    start_urls = [os.getenv("START_URLS")]

    def parse(self, response):
        pass
