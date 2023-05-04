#!/usr/bin/env python3
##
##
try:
    with open('filenotfound') as f:
        for line in f:
            print(line.strip())
except (FileNotFoundError, TypeError) as MissingFileError:
#except FileNotFoundError as MissingFileError:
    print(type(MissingFileError))
    print('File does not exist-->' + str(MissingFileError))
    #print('Hey we have an issue. This file does not exist')
    exit(99)

print('Yep, we are still running python from this module')
