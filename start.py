#!/usr/bin/env python
#-*- coding: utf-8 -*-

import web
from gis import GIS
from corelib.mako import render

urls = (
    '/', 'index',
    '/hello/(.+)', 'hello'
    )

class index:
    def GET(self):
        gis = GIS()
        issues = gis.get_user_issues()
        return render.index(issues = issues)

class hello:
    def GET(self, name):
        print name
        return render.hello(name = name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
