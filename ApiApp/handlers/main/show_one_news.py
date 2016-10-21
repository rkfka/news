#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import urllib

import json
from ApiApp.handlers.base import WebBaseHandler


class ShowOneNewsHandler(WebBaseHandler):
    def get(self, id_news, *args, **kwargs):
        item = id_news
        one_news = urllib.urlopen("http://www.servicefarsi.com/api/news/6678735804226/7/item="+item)
        one_news = one_news.read()
        one_news = json.loads(one_news)
        self.render("show_one_news.html", one_news=one_news['res'])
