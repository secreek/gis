#!/usr/bin/env python
#-*- coding: utf-8 -*-

from collections import OrderedDict

RELATION_ASSIGNED = 'assigned'
RELATION_CREATED = 'created'
RELATION_MENTIONED = 'mentioned'
RELATION_SUBSCRIBED = 'subscribed'

STATE_OPEN = 'open'
STATE_CLOSED = 'close'

ASSIGNED = 'Assigned'
CREATED = 'Created'
MENTIONED = 'Mentioned'
SUBSCRIBED = 'Subscribed'
TODAY = 'Today'

ISSUES_URL_MAPPING = OrderedDict()
ISSUES_URL_MAPPING[TODAY] = '/'
ISSUES_URL_MAPPING[ASSIGNED] = '/assigned'
ISSUES_URL_MAPPING[CREATED] = '/created'
ISSUES_URL_MAPPING[MENTIONED] = '/mentioned'
ISSUES_URL_MAPPING[SUBSCRIBED] = '/subscribed'
