#!/usr/bin/env python
# coding=utf-8


def showMaxfacor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            # print 'largest factor of %d is %d' % (num, count)
            break
        count -= 1

    else:
        print num,


for eachNum in range(1, 1000):
    showMaxfacor(eachNum)
