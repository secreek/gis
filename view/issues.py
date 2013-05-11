#!/usr/bin/env python
#-*- coding: utf-8 -*-

from model.gis import GIS
from corelib.consts import ASSIGNED, CREATED, MENTIONED, SUBSCRIBED
from corelib.consts import (RELATION_ASSIGNED, RELATION_CREATED,
        RELATION_MENTIONED, RELATION_SUBSCRIBED, STATE_OPEN, STATE_CLOSED)

from corelib.mako import render
import web

class IssuesPageBase:
    active_item = ASSIGNED
    relation = RELATION_ASSIGNED

    def GET(self):
        gis = GIS()
        issues_closed = gis.get_user_issues(self.relation, STATE_CLOSED)
        issues = gis.get_user_issues(self.relation, STATE_OPEN)
        return render.issues(issues = issues, issues_closed = issues_closed,
            active = self.active_item)

class AssignedIssues(IssuesPageBase):
    active_item = ASSIGNED
    relation = RELATION_ASSIGNED

class CreatedIssues(IssuesPageBase):
    active_item = CREATED 
    relation = RELATION_CREATED

class MentionedIssues(IssuesPageBase):
    active_item = MENTIONED
    relation = RELATION_MENTIONED

class SubscribedIssues(IssuesPageBase):
    active_item = SUBSCRIBED
    relation = RELATION_SUBSCRIBED
