#!/usr/bin/env python3
##
##
def readfile(filename):
    try:
        f=open(filename)
    except FileNotFoundError as MyException:
        print('Error caught --->' + str(MyException))
    else:
        for line in f:
            print(line.strip())
    finally:
        try:
            f.close()
        except UnboundLocalError as ErrorType:
            print('Error Caught -->', ErrorType)

def main():
    filename = input('Enter the filename: ')
    readfile(filename)

if __name__ == '__main__':
    main()


