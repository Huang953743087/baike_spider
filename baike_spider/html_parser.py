#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import re
from urllib import parse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):#对传入参数进行检测并匹配
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):#匹配新的url
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):#匹配新的标题与简介
        #class="lemmaWgt-lemmaTitle-title",

        res_data ={}
        res_data['url']=page_url
        #匹配标题
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        if title_node is None:
            return
        res_data['title']=title_node.get_text()
        #class="lemma-summary"
        #匹配简介
        summary_node = soup.find('div',class_="lemma-summary")
        if summary_node is None:
            return
        res_data['summary'] = summary_node.get_text()
        return res_data
