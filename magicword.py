#!/usr/bin/env python3
##
##
attempts = 0
magicWord = 'cisco'

while True:
    word = input('Please enter the magic word: ')
    attempts +=1 
    if magicWord == word.lower():
        break
    else:
        print('No, but are you getting closer!')

print('Congratulations, you guessed the magic word in ' + str(attempts) + ' tries')

##
##End of file.. 
