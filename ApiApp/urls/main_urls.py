#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ApiApp.handlers.main import show_news, show_one_news

__author__ = 'ReS4'

url_patterns = [
    ("/show_news", show_news.ShowNewsHandler, None, "show_news"),
    ("/show_one_news/([\w+]-(\d+))", show_one_news.ShowOneNewsHandler, None, "a:show_one_news"),
]
