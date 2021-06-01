# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id              = scrapy.Field()
    imdb_url        = scrapy.Field()
    title           = scrapy.Field()
    rating          = scrapy.Field()
    year            = scrapy.Field()
    vote            = scrapy.Field()
    metascore       = scrapy.Field()
    star            = scrapy.Field()
    certificate     = scrapy.Field()
    description     = scrapy.Field()
    director        = scrapy.Field()
    runtime         = scrapy.Field()
    genre           = scrapy.Field()
    pass
