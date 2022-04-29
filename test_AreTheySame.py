from AreTheySame import *

def test_IsItInput():
    assert IsItInput([100, 121], [100, 121]) == True

def test_IsItInput_false_1():
    assert IsItInput(1234, [100, 121]) == False

def test_IsItInput_false_2():
    assert IsItInput([100, 121], 1234) == False

