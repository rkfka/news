#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import urllib

import json
from ApiApp.handlers.base import WebBaseHandler


class ShowNewsHandler(WebBaseHandler):
    def get(self, *args, **kwargs):
        li_ostan = urllib.urlopen("http://www.servicefarsi.com/api/news/6678735804226/2/")
        li_ostan = li_ostan.read()
        li_ostan = json.loads(li_ostan)

        li_khabars_o = urllib.urlopen("http://www.servicefarsi.com/api/news/6678735804226/4/item=20,page=1")
        li_khabars_o = li_khabars_o.read()
        li_khabars_o = json.loads(li_khabars_o)

        li_khabars_iran = urllib.urlopen("http://www.servicefarsi.com/api/news/6678735804226/6/subject=ایران,page=1")
        li_khabars_iran = li_khabars_iran.read()
        li_khabars_iran = json.loads(li_khabars_iran)

        self.render("show_news.html", li_o=li_ostan['res'], li_khabars_o=li_khabars_o['res'],
                    li_khabars_iran=li_khabars_iran['res'])

    def post(self, *args, **kwargs):
        id_province = self.get_argument("id_province", None)
        li_khabars_o = urllib.urlopen("http://www.servicefarsi.com/api/news/6678735804226/4/page=1,item="+id_province)
        li_khabars_o = li_khabars_o.read()
        li_khabars_o = json.loads(li_khabars_o)
        self.write({"data": li_khabars_o})
