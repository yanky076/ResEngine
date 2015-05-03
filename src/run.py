#!/usr/bin/env python
# coding: utf-8

import cherrypy
from pyjsonrpc.cp import CherryPyJsonRpc, rpcmethod

class ResEngine(CherryPyJsonRpc):
    @rpcmethod
    def add(self, a, b):
        return a + b

    index = CherryPyJsonRpc.request_handler

cherrypy.config.update("../conf/server.conf")
cherrypy.tree.mount(ResEngine(), "/res", config="../conf/app.conf")
if hasattr(cherrypy.engine, 'block'):
    # 3.1 syntax
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    # 3.0 syntax
    cherrypy.server.quickstart()
    cherrypy.engine.start()