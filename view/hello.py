#!/usr/bin/env python
#-*- coding: utf-8 -*-

class hello:
    def GET(self, name):
        print name
        return render.hello(name = name)
