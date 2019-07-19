#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-04 10:47:05
# Project: 36kr

from pyspider.libs.base_handler import *
import re

class Handler(BaseHandler):
    crawl_config = {
        "timeout" : 1000
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36",
        "Referer":"https://jd.com/",
        "Content-Type":"text/html; charset=utf-8"
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://36kr.com/', headers = self.headers,fetch_type='js',validate_cert=False,callback=self.detail_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        pass

    @config(priority=2)
    def detail_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            s = each.attr.href
            if "http://" in s:
                s = "https://" + s.split("http://")[1]
            if "from=" in s:
                s = s.split("?from=")[0]
            if "/p/" in s and "baidu.com" not in s and "36kr.com" in s:
                self.crawl(s,headers = self.headers,callback=self.detail_page,fetch_type='js',validate_cert=False)
        mtime = re.findall("[\d]{4}-[\d]{1,2}-[\d]{1,2}",response.doc('.time').text())[0]
        if "/p/" in response.url:
            return {
                "url": response.url,
                "title": response.doc('title').text(),
                "len":len(response.doc("body").text()),
                "mtime": mtime
                
            }
