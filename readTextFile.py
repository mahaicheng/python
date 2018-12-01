#!/usr/bin/env python
# coding=utf-8

'readTextFile.py -- read and display text file'


# get file name
fname = raw_input('Enter file name: ')
print

# attempt to open file for reading
try:
    fd = open(fname, 'r')

except IOError, e:
    print "*** file open error:", e
else:
    # display contents to the screen
    for eachLine in fd:
        print eachLine,

    fd.close()
