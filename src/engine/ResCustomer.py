#!/usr/bin/env python
# coding: utf-8

import json
import os
from ResConstants import ResConstants
from encoder import XML2Dict

class ResCustomer():

    customerDict = {}

    class Labels():
        CUSTOMER_NAME = "customerName"
        SERVER_LIST = "servers"
        SERVER_NAME = "server_name"

    class CustomerServer():
        server = {}
        attributes = {}

    def __init__(self, customerName):
        self.setCustomerName(customerName)
        self.prepareServersForCustomer()

    def getCustomerName(self):
        return self.customerDict[self.Labels.CUSTOMER_NAME]

    def setCustomerName(self, customerName):
        self.customerDict[self.Labels.CUSTOMER_NAME] = customerName

    def prepareServersForCustomer(self):
        self.customerDict[self.Labels.SERVER_LIST] = []
        if self.customerDict.has_key(self.Labels.CUSTOMER_NAME):
            customerDbRoot = "%s/%s" % (ResConstants.FileLocations.RML_DATABASE, self.getCustomerName())
            if os.path.isdir(customerDbRoot):
                xml2dict = XML2Dict()
                for dirpath, dirs, files in os.walk(customerDbRoot):
                    for file in files:
                        serverObject = self.CustomerServer
                        serverObject.server[self.Labels.SERVER_NAME] = file
                        with open("%s/%s" % (dirpath, file), "r") as fileObject:
                            serverObject.attributes = xml2dict.parse(fileObject.read())
                        self.customerDict[self.Labels.SERVER_LIST].append(serverObject)

    def getPreparedServers(self):
        return self.customerDict[self.Labels.SERVER_LIST]

    def toJson(self):
        return json.dumps(self.customerDict)

    def get(self):
        return self.customerDict

    '''
    def __init__(self, customerName):
        Thread.__init__(self)
        self.customerName = customerName

    def run(self):
        logger = logging.getLogger("MAIN.RESENGINE.RESCUSTOMER")
        logger.debug("Customer name is %s" % (self.customerName))
    '''