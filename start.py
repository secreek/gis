#!/usr/bin/env python
#-*- coding: utf-8 -*-

import web
from corelib.mako import render
from view.index import index
from view.hello import hello

urls = (
    '/', 'index',
    '/hello/(.+)', 'hello'
    )

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
