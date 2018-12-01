#!/usr/bin/env python
# coding=utf-8

from urllib import urlretrieve


def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue

    else:
        return eachLine


def firstLast(webPage):
    f = open(webPage)
    lines = f.readlines()
    f.close()

    print firstNonBlank(lines)
    lines.reverse()
    print firstNonBlank(lines)


def download(url="http://www.mahaicheng.com", process=firstLast):
    try:
        retVal = urlretrieve(url)[0]
    except IOError:
        retVal = None

    if retVal:
        process(retVal)


if __name__ == '__main__':
    download()
