#!/usr/bin/env python
# coding: utf-8

import logging
from pyjsonrpc.cp import CherryPyJsonRpc, rpcmethod
from ResConstants import ResConstants
from ResCustomer import ResCustomer
from ResCache import ResCache
import threading
import json

class ResEngine(CherryPyJsonRpc):

    lock = threading.Lock()

    @rpcmethod
    def prepareCustomer(self, customerName):
        logger = logging.getLogger("MAIN.RESENGINE")
        if ResCache.preparedCustomers.has_key(customerName):
            logger.debug("%s is already prepared." % (customerName))
        else:
            customerObject = ResCustomer(customerName)
            with self.lock:
                ResCache.preparedCustomers[customerName] = customerObject
                logger.debug("Prepared customer %s" % (customerName))
        return ResConstants.JsonRpcResponse.SUCCESS


    @rpcmethod
    def executeServersForCustomer(self, customerName, *serverList):
        with self.lock:
            if ResCache.preparedCustomers.has_key(customerName):
                customerObject = ResCache.preparedCustomers[customerName]
                response = []
                for serverName in serverList:
                    serverObject = {}
                    serverObject["server_name"] = serverName
                    serverObject["status"] = "RML MISSING"
                    for s in customerObject.getPreparedServers():
                        if s.server["server_name"] == serverName:
                            serverObject["status"] = "EXECUTING"
                            break
                    response.append(serverObject)
                return json.dumps(response)
            else:
                return "Customer must be prepared first"

    index = CherryPyJsonRpc.request_handler