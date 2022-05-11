from AreTheySame import *

def test_IsItInput():
    assert IsItInput([100, 121], [100, 121]) == True

def test_IsItInput_false_1():
    assert IsItInput(1234, [100, 121]) == False

def test_IsItInput_false_2():
    assert IsItInput([100, 121], 1234) == False

def test_IsItNotEmpty_1():
    assert IsItNotEmpty([]) == False

def test_IsItNotEmpty_2():
    assert IsItNotEmpty(None) == False

def test_IsItNoEmpty_3():
    assert IsItNotEmpty([10, 12, 14]) == True

def test_comp_1():
    assert comp([11, 12, 3], [121, 144, 9]) == True

def test_comp_2():
    assert comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]) == True

def test_comp_3():
    assert comp([121, 144, 19, 161, 19, 144, 19, 11], [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]) == False

def test_comp_4():
    assert comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]) == False
