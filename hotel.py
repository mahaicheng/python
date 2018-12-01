#!/usr/bin/env python
# coding=utf-8


class HotelRoom(object):
    'Hotel room calculator'

    def __init__(self, rt, sales=0.085, rm=0.1):
        '''HotelRoom default arguments:
        sales tax == 8.5% and room tax == 10%'''

        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        'calculate total; default to daily rate'
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)

        return float(days) * daily
