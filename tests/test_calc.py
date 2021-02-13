#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytest_workshop
----------------------------------

Tests for `pytest_workshop` module.
"""
import pytest 
from pytest_workshop.calc import Calc 

################################################
#  Test the "add" method 
################################################
def testAddTwoNumbers():
    c = Calc()
    result = c.add(4,5)

    assert result == 9

def testAddManyNumbers():
    c = Calc()
    s = range(100)
    result = c.add(*s)

    assert result == 4950 

################################################
#  Test the "subtract" method 
################################################
def testSubtractTwoNumbers():
    assert Calc().subtract(10,3) == 7

def testSubtractTwoNegativeNumbers():
    assert Calc().subtract(-10,-3) == -7

def testSubtractNegativeFromPositiveNumber():
    assert Calc().subtract(10,-3) == 13

################################################
#  Test the "multiply" method 
################################################
def testMultiplyTwoNumbers():
    assert Calc().multiply(6,4) == 24

def testMultiplyManyNumbers():

    s = range(1,10)
    assert Calc().multiply(*s) == 362880

def testMultiplyByZeroRaiseException():

    with pytest.raises(ValueError):
        Calc().multiply(3,0)

################################################
#  Test the "divide" method 
################################################
def testDivideTwoNumbers():
    assert Calc().divide(22,2) == 11

def testDivideReturnsFloats():
    assert Calc().divide(11,2) == 5.5

def testDivideByZeroReturnsInf():
    assert Calc().divide(11,0) == "inf"

################################################
#  Test the "average" method 
################################################
def testAverageIterable():
    assert Calc().average([2,5,12,98]) == 29.25

def testAverageRemovesUpperOutliers():
    assert Calc().average([2,5,12,98], ut=90) == pytest.approx(6.33333)

def testAverageRemovesUpperOutliersEquality():
    assert Calc().average([2,5,12,98], ut=12) == pytest.approx(6.33333)

def testAverageRemovesLowerOutliers():
    assert Calc().average([2,5,12,98], lt=10) == pytest.approx(55)

def testAverageRemovesLowerOutliersEquality():
    assert Calc().average([2,5,12,98], lt=10) == pytest.approx(55)

def testAverageManagesEmptyIterable():
    with pytest.raises(ValueError):
        Calc().average([])

def testAverageManagesEmptyIterableAfterOutliersRemoval():
    with pytest.raises(ValueError):
        Calc().average([12,98], lt=15, ut=90)

def testAverageManagesEmptyIterableWithThresholds():
    with pytest.raises(ValueError):
        Calc().average([], lt=15, ut=90)

def testAverageDoesnotWorkWithNonIterableTypes():
    with pytest.raises(TypeError):
        Calc().average(123)

def testAverageManagesZeroValueLowerThreshold():
    assert Calc().average([-1,0,1], lt=0) == 0.5

def testAverageManagesZeroValueUpperThreshold():
    assert Calc().average([-1,0,1], ut=0) == -0.5

