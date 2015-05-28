# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import BaseSgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from googlecode.items import GooglecodeItem
from scrapy.http import Request
import json
sonraki=''
year=None
items =[]
"""
kullanisi scrapy crawl code -o data2011.json -a year=2011
"""
class CodeSpider(CrawlSpider):
    name = "code"
    allowed_domains = ["google-melange.com"]

    def __init__(self,year, *args, **kwargs):
        globals()['year'] =year
        super(CodeSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.google-melange.com/gsoc/org/list/public/google/gsoc%s' % year]

    def parse(self, response):
        url = "https://www.google-melange.com/gsoc/org/list/public/google/gsoc"+year+"?fmt=json&PageSpeed=noscript"
        #print "degişimi görelim :  " + sonraki
        return Request(url, callback=self.parse_stores)

    def parse_stores(self, response): # json yakalayıp parse ediyor.
        data = json.loads(response.body)
        for store in data['data'][sonraki]:
            item=GooglecodeItem()
            #global org_id,keys,tags,names,ideas
            org_id = store["columns"]['org_id']
            sec_url="http://www.google-melange.com/gsoc/org2/google/gsoc"+year+"/"+org_id+"?fmt=json&limit=100&idx=0&_=1430396371908"
            yield Request(sec_url,callback=self.secparse)
            #dic = {'idea':store["columns"]['ideas'],'org_id': store["columns"]['org_id']}
            #print dic
            yield GooglecodeItem(
                idea = store["columns"]['ideas'],
                org_id = store["columns"]['org_id'],
                key = store["columns"]['key'],
                tag = store["columns"]['tags'],
                name = store["columns"]['name']
                )  
        global sonraki
        sonraki = data['next']
        if(sonraki!="done"):
            base_url = "https://www.google-melange.com/gsoc/org/list/public/google/gsoc"+year+"?fmt=json&start=%s&PageSpeed=noscript"
            yield Request(base_url % sonraki, callback=self.parse_stores)

    def secparse(self, response):
        data = json.loads(response.body)
        for store in data['data']['']:
            link = store["operations"]["row"]["link"]
            #print link
            description_url="http://www.google-melange.com%s"
            yield Request(description_url % link, callback=self.description_parse)

    def description_parse(self,response):
        hxs = HtmlXPathSelector(response)
        global descriptions,basliks
        descriptions=hxs.select('//p[contains(@class,"description")]/text()').extract()
        basliks=hxs.select('//h1[contains(@id,"project-page-title")]/text()').extract()
        yield GooglecodeItem(description = descriptions,
                            title = basliks
                            )
