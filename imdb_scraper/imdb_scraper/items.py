# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ImdbScraperItem(Item):
    title = Field()
    year = Field()
    ratings = Field()