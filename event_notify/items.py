import scrapy


class EventItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    schedule = scrapy.Field()
    place = scrapy.Field()
    plices = scrapy.Field()

    def format_tweet(self) -> str:
        text = "\n".join(
            [self["schedule"], self["place"], *self["plices"], self["url"]]
        )
        return "\n".join([self["title"][: 140 - len(text) - len("\n")], text])
