#!/usr/bin/env python
#-*- coding: utf-8 -*-

from corelib.mako import render

class hello:
    def GET(self, name):
        return render.hello(name = name)
