# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import MySQLdb as mdb
import sys

# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DBWritePipeline(object):

    def __init__(self):
     try:
       self.con = mdb.connect('localhost', 'root', '', 'web_mining');
       self.cur = self.con.cursor()
       self.cur.execute("SELECT * FROM company")
       rows = self.cur.fetchall()
       self.titles = dict()
       for row in rows:
         self.titles[row[1]] = row[0]

     except mdb.Error, e:
       print "Error %d: %s" % (e.args[0],e.args[1])
       sys.exit(1)

    def process_item(self, item, spider):
     try:
       if not (item["name"] in self.titles):  # we already knew this film
          self.cur.execute("INSERT INTO company VALUES('%s')" % item["name"])
          self.titles[item["name"]] = self.cur.lastrowid

       self.cur.execute("INSERT INTO project(idea_link,key,tag) \
                   VALUES('%s','%s','%s')" %
                     (self.titles[item["ideas"]],
                      int(item["key"]), item["tag"])
                     )
       """self.cur.execute("INSERT INTO year(year) \
                   VALUES(%d)" %
                     (self.titles[item["ideas"]],
                      int(item["key"]), item["tag"])
                     )
       """
       self.con.commit()
       return item

     except mdb.Error, e:
       print "Error %d: %s" % (e.args[0],e.args[1])
       sys.exit(1)
