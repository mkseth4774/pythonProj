#!/usr/bin/env python3
##
##
class NetworkNode:
    '''This is my class'''

    def __init__(self, serialNumber, ip, os, location='Cisco Building#14, SanJose, CA'):
        '''This is my class Constructor function'''
        self.serialNumber = serialNumber
        self.ip = ip
        self.os = os
        self.location = location

    def NodeInfo(self):
        '''This function prints out the Object attributes, data'''
        print('-' * 79)
        return '{} {} {} {}'.format(self.serialNumber, self.ip, self.os, self.location)

##
##End of file....
