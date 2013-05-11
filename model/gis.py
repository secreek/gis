#!/usr/bin/env python
#-*- coding: utf-8 -*-

try:
    import local_config as config
except ImportError:
    import config
from pygithub3 import Github
from corelib.consts import (RELATION_ASSIGNED, RELATION_CREATED,
        RELATION_MENTIONED, RELATION_SUBSCRIBED, STATE_OPEN, STATE_CLOSED)
from collections import defaultdict
from datetime import date, datetime

class GIS:

    def __init__(self):
        self.gh = Github(login=config.username, password=config.password)

    def get_user_issues(self, relation=RELATION_ASSIGNED, state=STATE_OPEN,
            since=None):
        return self.gh.issues.list(filter=relation, state=state, since=since).all()

    def get_all_issues(self, since=None):
        issues_by_relation_and_state = defaultdict(dict)
        relations = ( RELATION_ASSIGNED, RELATION_CREATED, 
                RELATION_MENTIONED, RELATION_SUBSCRIBED,
            )
        states = (STATE_OPEN, STATE_CLOSED,)

        for relation in relations:
            for state in states:
                issues_by_relation_and_state[relation][state] = self.get_user_issues(relation,
                        state, since)
        return issues_by_relation_and_state

    def get_all_issues_since(self, date):
        #datetime type is needed
        return self.get_all_issues(since=date)

    def get_all_issues_today(self):
        t = date.today()
        today = datetime.fromordinal(t.toordinal())
        return  self.get_all_issues_since(today)

def list_issues(issues):
    def print_line(name, value):
        print '%s: %s' % (name, value)

    for issue in issues:
        print '____________'
        print_line('url', issue.html_url)
        print_line('content', issue.body)
        print_line('created_at', issue.created_at)
        print_line('updated_at', issue.updated_at)
        print_line('close_at', issue.closed_at)
        print_line('assignee', str(issue.assignee))


def main():
    gis = GIS()
    issues_subscribed = gis.get_user_issues(relation='subscribed')
    issues_assigned = gis.get_user_issues()
    print 'subscribed issues:'
    list_issues(issues_subscribed)
    print 'assignd issues:'
    list_issues(issues_assigned)

if __name__ == '__main__':
    main()
