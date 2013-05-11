#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model.gis import GIS

class index:
    def GET(self):
        gis = GIS()
        issues = gis.get_user_issues()
        return render.index(issues = issues)
