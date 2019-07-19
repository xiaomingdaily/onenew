#!usrbinenv python
# -- encoding utf-8 --
# Created on 2018-07-28 191645
# Project 4hou

from pyspider.libs.base_handler import 


class Handler(BaseHandler)
    crawl_config = {
    }

    @every(minutes=24  60)
    def on_start(self)
        self.crawl('https4hou.winwordpress', callback=self.index_page, validate_cert=False)

    @config(age=10  24  60  60)
    def index_page(self, response)
        for each in response.doc('a[href^=http]').items()
            s = each.attr.href
            if paged= in s
                self.crawl(each.attr.href, callback=self.index_page, validate_cert=False)
            elif p= in s
                self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response)
        return {
            url response.url,
            title response.doc('title').text(),
            bodyresponse.doc('body').text(),
            lenlen(response.doc('body').text())
        }
