#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-03 20:35:18
# Project: youtube

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36",
        "Content-Type":"application/json; charset=utf-8",
        "timeout" : 1000,
        "proxy" : "127.0.0.1:1080"
    }
    def get_proxy():
        return requests.get("http://123.207.35.26:5010/get/").content
    
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.youtube.com/', callback=self.detail_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            s = each.attr.href
            if "watch?v=" in s and "#" not in s and "&list=" not in s:
                self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)      
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "view":response.doc('.watch-view-count').text().split(" ")[0],
            "description":response.doc('#watch-description-text > p').text(),
        }
