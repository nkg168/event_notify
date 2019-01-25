# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import redis
from logging import getLogger
import twitter
from scrapy.exceptions import DropItem

# store eventID
REDIS_KEY = "events"
logger = getLogger(__name__)


class ValidationPipeline(object):
    def process_item(self, item, spider):
        for v in item.values():
            if not v:
                raise DropItem(f"field is empty!!")
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
            raise DropItem("this is tweeted")
        return item


class TweetPipeline(object):
    def open_spider(self, spider):
        auth = twitter.OAuth(
            consumer_key=os.getenv("CONSUMER_KEY"),
            consumer_secret=os.getenv("CONSUMER_SECRET"),
            token=os.getenv("TOKEN"),
            token_secret=os.getenv("TOKEN_SECRET"),
        )
        self.t = twitter.Twitter(auth=auth)

    def process_item(self, item, spider):
        try:
            self.t.statuses.update(status=item.format_tweet())
        except:
            # 重複等のエラー無視
            logger.exception("tweet失敗")
        else:
            logger.info("tweet成功")
