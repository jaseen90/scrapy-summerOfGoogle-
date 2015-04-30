# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import Join

class GooglecodeItem(Item):
    # define the fields for your item here like:
    name = Field()
    tag = Field()
    key = Field()
    idea = Field()
    org_id=Field()
    nextt=Field()

    project_name = Field()
    project_link = Field()

    description= Field()
    title= Field()
    #tags = Field()
