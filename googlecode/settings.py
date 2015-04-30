# -*- coding: utf-8 -*-

# Scrapy settings for googlecode project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'googlecode'

SPIDER_MODULES = ['googlecode.spiders']
NEWSPIDER_MODULE = 'googlecode.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'googlecode (+http://www.yourdomain.com)'
DOWNLOAD_DELAY = 0.5
#ITEM_PIPELINES = {'googlecode.pipelines.DBWritePipeline': 500}
