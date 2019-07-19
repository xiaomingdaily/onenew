#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-01-26 22:53:04
# Project: pedaily_cn

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.pedaily.cn/all/1', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            s = each.attr.href
            if "/all/" in s:
                self.crawl(s, callback=self.index_page)
            elif "/p/" in s or "/2018" in s or "/2017" in s:
                self.crawl(s, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "time":response.doc('.news-show-title .date').text().split(" ")[0],
            "content":len(response.doc('.news-content > p').text()),
        }
