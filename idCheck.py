#!/usr/bin/env python
# coding=utf-8

import string

alpha = string.letters + '_'
nums = string.digits

str = raw_input("Identify: ")

if len(str) > 1:
    if str[0] not in alpha:
        print 'invalid: first symbol must be alphabetic'
    else:
        for otherChar in str[1:]:
            if otherChar not in alpha + nums:
                print 'invalid: remaining symbol must be alphabetic'
                break
        else:
            print "okay as an Identifier"
