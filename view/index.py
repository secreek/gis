#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model.gis import GIS
from corelib.mako import render
import web

class Index:
    def GET(self):
        #TODO: show today's issues
        raise web.redirect('/assigned')
        '''
        gis = GIS()
        issues_by_relation_and_state = gis.get_all_issues()
        print gis.get_all_issues_today()
        print issues_by_relation_and_state
        issues = gis.get_user_issues()
        return render.index(issues = issues)
        '''
