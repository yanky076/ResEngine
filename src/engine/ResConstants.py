#! /usr/bin/env python
#coding: utf-8

class ResConstants():

    # JSON RPON standard responses
    class JsonRpcResponse():
        SUCCESS = "SUCCESS"
        FAILURE = "FAILURE"

    # file locations and directories
    class FileLocations():
        # all file locations are from root directory
        RML_DATABASE = "/home/varunsondhi/PycharmProjects/ResEngine/db/rmls"