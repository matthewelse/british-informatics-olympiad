"""Test cases for 2016 Q3"""

import q3

def test_case0():
    assert q3.solve(100, 2, 13) == 4

def test_case1():
    assert q3.solve(20, 2, 3) == 2

def test_case2():
    assert q3.solve(20, 2, 13) == 4

def test_case3():
    assert q3.solve(100, 73, 89) == 2

def test_case4():
    assert q3.solve(100, 19, 97) == 7

def test_case5():
    assert q3.solve(1000, 3, 971) == 9

def test_case6():
    assert q3.solve(2000, 977, 997) == 4

def test_case7():
    assert q3.solve(5000, 83, 3643) == 10

def test_case8():
    assert q3.solve(614700, 3643, 90149) == 18

def test_case9():
    assert q3.solve(987654, 3643, 90149) == 16

def test_case10():
    assert q3.solve(1000000, 2, 968137) == 18

def test_case11():
    assert q3.solve(1000000, 993851, 995387) == 3
