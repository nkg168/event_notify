import os
from urllib.parse import urljoin
import scrapy
from scrapy_selenium import SeleniumRequest
from event_notify.items import EventItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class EventsiteSpider(scrapy.Spider):
    name = "eventsite"
    allowed_domains = [os.getenv("ALLOWED_DOMAINS")]
    start_urls = [os.getenv("START_URLS")]
    root_url = os.getenv("ROOT_URL")

    def parse(self, response):
        for url in response.css(
            "header.c-eventSummary-header > a::attr('href')"
        ).extract():
            yield SeleniumRequest(
                wait_time=5,
                wait_until=EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.c-eventSummary-stats")
                ),
                url=urljoin(self.root_url, url),
                callback=self.parse_event,
            )
        next_page = response.css(
            'li.page > a[rel="next"]::attr("href")'
        ).extract_first()
        if next_page:
            yield SeleniumRequest(
                url=urljoin(self.root_url, next_page), callback=self.parse
            )

    def parse_event(self, response):
        yield EventItem(
            url=response.url,
            id=response.url.split("/")[-2],
            title=response.css("h1.c-eventSummary-title > span::text").extract_first(),
            place="/".join(response.css("span.left-address > a::text").extract()),
            schedule=(
                "".join(
                    response.css("span.c-eventSummary-datetime > spam::text").extract()
                )
                or ""
            )
            + response.css("span.c-eventSummary-datetime > span::text").extract_first(),
            plices=[
                ":".join(
                    [
                        (dl.css("dt > span::text").extract_first() or ""),
                        (dl.css("dd > span > b::text").extract_first() or ""),
                        (dl.css("dd > span::text").extract_first() or ""),
                    ]
                )
                for dl in response.css(
                    "div.c-sectionUnit-body > div.c-eventSummary-stats > dl"
                )
                if ("u-icon-male" in dl.css("dt > span::attr(class)").extract_first())
            ],
        )
