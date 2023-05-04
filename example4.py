#!/usr/bin/env python3
##
##
class NetworkNode:
    '''This is my class'''

    #Declare Class Variable
    nodeType = 'IOT'

    def __init__(self, serialNumber, ip, os, location='Cisco Building#14, SanJose, CA', username='admin',password='cisco'):
        '''This is my class Constructor function'''
        self.serialNumber = serialNumber
        self.ip = ip
        self.os = os
        self.location = location
        self.username = username
        self.password = password

    def NodeInfo(self):
        '''This function prints out the Object attributes, data'''
        return '{:15} {:10} {:17} {:40} {:10} {:15}'.format(
							    self.serialNumber, 
							    self.ip, 
							    self.os, 
						            self.location, 
							    self.username, 
						            self.password
						           )

    def NodeInfo2(self):
        '''This function prints out the Class Variable'''
        return 'This node is of type: {}'.format(self.nodeType)

#iInstantiating the node01 Object 
node01 = NetworkNode('FTX98274242', '192.168.1.1','nexus 4.12(YBS)2.5', 'superuser')

print()
print('{:15} {:10} {:17} {:40} {:10} {:15}'.format('SerialNumber', 'IP', 'IOS', 'Location', 'User','Password'))
print('-' * 100)
print(node01.NodeInfo())
print()
print(node01.NodeInfo2())

##
##End of file....
