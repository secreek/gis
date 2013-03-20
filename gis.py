#!/usr/bin/env python
#-*- coding: utf-8 -*-

try:
    import local_config as config
except ImportError:
    import config
from pygithub3 import Github

class GIS:

    def __init__(self):
        self.gh = Github(login=config.username, password=config.password)

    def get_user_issues(self, relation='assigned', state='open'):
        return self.gh.issues.list(filter=relation, state=state).all()

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
