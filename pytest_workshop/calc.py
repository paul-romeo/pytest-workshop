# -*- coding: utf-8 -*-
from math import prod
from statistics import mean

class Calc: 
    def add(self, *s):
        return sum(s)

    def subtract(self, a, b):
        return a - b

    def multiply(self, *s):
        if 0 in s: 
            raise ValueError 
        
        return prod(s)

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "inf"

    def average(self, numbersList, lt=None, ut=None):
        # Notes: lt: lower threshold, ut: upper threshold 

        if not len(numbersList):
            raise ValueError
        if ut is None:
            ut = max(numbersList)
        if lt is None:
            lt = min(numbersList)

                
        revisedNumbersList = [x for x in numbersList if (x <= ut and x >=lt)]
        # print(f'revisedNumbersList: {revisedNumbersList}')
        if not len(revisedNumbersList): 
            raise ValueError
        return mean(revisedNumbersList)      
        

        
