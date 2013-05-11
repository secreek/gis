#!/usr/bin/env python
#-*- coding: utf-8 -*-

from corelib.mako import render

class Hello:
    def GET(self, name):
        return render.hello(name = name)
