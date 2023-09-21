# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名字
    title = scrapy.Field()
    # 工作职责
    responsibility = scrapy.Field()
    # 工作要求
    requirement = scrapy.Field()
    pass