#!/usr/bin/env python
#-*- coding: utf-8 -*-

try:
    import local_config as config
except ImportError:
    import config
from pygithub3 import Github

def list_issues(issues):
    def print_line(name, value):
        print '%s: %s' % (name, value)

    for issue in issues:
        print '____________'
        print_line('url', issue.html_url)
        print_line('content', issue.body)
        print_line('comments', str(issue.comments))
        print_line('created_at', issue.created_at)
        print_line('updated_at', issue.updated_at)
        print_line('close_at', issue.closed_at)
        print_line('assignee', str(issue.assignee))


def main():
    gh = Github(login=config.username, password=config.password)
    issues_subscribed = gh.issues.list(filter='subscribed').all()
    issues_assigned = gh.issues.list().all()
    print 'subscribed issues:'
    list_issues(issues_subscribed)
    print 'assignd issues:'
    list_issues(issues_assigned)

if __name__ == '__main__':
    main()
