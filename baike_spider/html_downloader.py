#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import string
from urllib import request
from urllib.parse import quote
class HtmlDownloader(object):
    def download(self, url):#下载url
        if url is None:
            return None
        _url = quote(url,safe=string.printable)
        response=request.urlopen(_url)
        if response.getcode() != 200:
            return None
        return response.read()

