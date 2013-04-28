#!/usr/bin/env python
#-*- coding: utf-8 -*-

from gis import GIS
from corelib.mako import render

urls = (
    '/', 'index'
    )

class index:
    def GET(self):
        gis = GIS()
        issues = gis.get_user_issues()
        return render.index(issues = issues)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
