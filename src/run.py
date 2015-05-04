#!/usr/bin/env python
# coding: utf-8

import cherrypy
from engine import ResEngine
import logging

# configuring logger
logger = logging.getLogger("MAIN")
logHandlerConsole = logging.StreamHandler()
logFormatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
logHandlerConsole.setFormatter(logFormatter)
logger.addHandler(logHandlerConsole)
logger.setLevel(logging.DEBUG)

# configuring and starting cherrypy engine
cherrypy.config.update("../conf/server.conf")
cherrypy.tree.mount(ResEngine.ResEngine(), "/res", config="../conf/app.conf")
cherrypy.engine.start()
cherrypy.engine.block()