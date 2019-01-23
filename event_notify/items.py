import scrapy


class EventItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
    schedule = scrapy.Field()
    plices = scrapy.Field()
    place = scrapy.Field()
