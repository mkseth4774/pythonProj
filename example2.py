#!/usr/bin/env python3
##
##

dmxSerialNumber = 'FTX8675309'
with open('nodes.txt') as f:
    for line in f:
        if dmxSerialNumber in line:
            pass
        print(line.strip())

##
##End of file
