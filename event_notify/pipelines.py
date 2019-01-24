# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import redis
from logging import getLogger
from scrapy.exceptions import DropItem

# store eventID
REDIS_KEY = "events"


class ValidationPipeline(object):
    def process_item(self, item, spider):
        for v in item.values():
            if not v:
                raise DropItem(f"empty_field!! {item.__dict__}")
        return item


class RedisPipeline(object):
    def open_spider(self, spider):
        self.r = redis.StrictRedis.from_url(
            os.environ.get("REDIS_URL"), None, charset="utf-8", decode_responses=True
        )
        self.evnets_old = self.r.smembers(REDIS_KEY)
        self.r.delete(REDIS_KEY)

    def process_item(self, item, spider):
        self.r.sadd(REDIS_KEY, item["id"])
        if item["id"] in self.evnets_old:
            raise DropItem(f"{item['id']} is tweeted")
        return item
