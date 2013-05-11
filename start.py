#!/usr/bin/env python
#-*- coding: utf-8 -*-

from view.index import index
from view.hello import hello
from corelib.server import GISServer

urls = (
    '/', 'index',
    '/hello/(.+)', 'hello'
    )

if __name__ == "__main__":
    server = GISServer(urls, globals())
    server.run()
