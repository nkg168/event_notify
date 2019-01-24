import scrapy


class EventItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    schedule = scrapy.Field()
    plices = scrapy.Field()
    place = scrapy.Field()
