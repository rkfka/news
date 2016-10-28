#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import urllib

import json
from ApiApp.handlers.base import WebBaseHandler


class ShowNewsHandler(WebBaseHandler):
    def get(self, *args, **kwargs):

        print("yes")
