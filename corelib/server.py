#!/usr/bin/env python
#-*- coding: utf-8 -*-

import web
from corelib.mako import render

class GISServer:

   #encapsulation for handle other event

    def __init__(self, urls, argvs):
        self.server = web.application(urls, argvs)
        self.server.notfound = self.notfound
        self.server.internalerror = self.internalerror

    def run(self):
        self.server.run()

    def notfound(self):
        #return web.notfound("Sorry, the page you were looking for was not
        #        found.")
        return web.notfound(render.notfound(name = 'Not Found'))

    def internalerror(self):
        return web.internalerror(render.internalerror(name = 'Internal Error'))


