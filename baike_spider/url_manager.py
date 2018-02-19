#!/usr/bin/env python3
#-*- coding: utf-8 -*-
class UrlManager(object):
    def __init__(self):
        self.new_urls=set()#用set以避免重复
        self.old_urls=set()
    def add_new_url(self, url):#添加url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):#批量添加url
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):#判断是否有新的url
        return len(self.new_urls) != 0

    def get_new_url(self):#读取新的url并转移到已读取
        new_nrl=self.new_urls.pop()
        self.old_urls.add(new_nrl)
        return new_nrl

