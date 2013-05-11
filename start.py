#!/usr/bin/env python
#-*- coding: utf-8 -*-

from view.index import Index
from view.hello import Hello
from corelib.server import GISServer
from view.issues import (AssignedIssues, CreatedIssues, MentionedIssues,
        SubscribedIssues)
from corelib.consts import ISSUES_URL_MAPPING, ASSIGNED, CREATED, MENTIONED, SUBSCRIBED

urls = (
    '/', 'Index',
    '/hello/(.+)', 'Hello',
    ISSUES_URL_MAPPING[ASSIGNED], 'AssignedIssues',
    ISSUES_URL_MAPPING[CREATED], 'CreatedIssues',
    ISSUES_URL_MAPPING[MENTIONED], 'MentionedIssues',
    ISSUES_URL_MAPPING[SUBSCRIBED], 'SubscribedIssues',
    )

if __name__ == "__main__":
    server = GISServer(urls, globals())
    server.run()
