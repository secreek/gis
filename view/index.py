#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model.gis import GIS
from corelib.mako import render

class index:
    def GET(self):
        gis = GIS()
        issues_by_relation_and_state = gis.get_all_issues()
        print issues_by_relation_and_state
        issues = gis.get_user_issues()
        return render.index(issues = issues)
