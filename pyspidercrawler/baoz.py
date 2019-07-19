#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-09-10 12:53:29
# Project: baozÅÀ³æÏîÄ¿

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://baoz.net', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            s = each.attr.href 
            if "#" in s or "baoz.net" not in s or "/tag/" in s or "/category/" in s:
                continue
            elif "/page/" in s:
                self.crawl(s, callback=self.index_page)
            else:
                self.crawl(s, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }