#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-07-29 21:37:33
# Project: freebuf

from pyspider.libs.base_handler import *
import re

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.freebuf.com/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        regex1=re.compile(r'\d+.html',re.IGNORECASE)
        for each in response.doc('a[href^="http"]').items():
            s = each.attr.href
            if "/page/" in s:
                self.crawl(s,callback=self.index_page)
            elif "#" not in s and len(regex1.findall(s))>0:
                self.crawl(s,callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "len": len(response.doc('body').text())
        }
