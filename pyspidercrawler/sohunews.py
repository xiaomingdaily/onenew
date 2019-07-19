#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-01-28 10:31:07
# Project: sohu_com

from pyspider.libs.base_handler import *

#todo:JS
class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://business.sohu.com/gskb/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            s = each.attr.href
            if "gskb/index_" in s:
                self.crawl(s, callback=self.index_page)
            elif "business.sohu.com/2017" in s or "business.sohu.com/2018" in s:
                self.crawl(s, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "time":response.doc('[itemprop="datePublished"]').text(),
            "content":len(response.doc('[itemprop="articleBody"] > p').text())
        }
