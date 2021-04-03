"""Test cases for 2016 Q2"""
import q2

def test_case0():
    assert q2.format_solution(q2.solve(8, [0], 6), sep='') == """
00100
01210
00100
00000
00000""".lstrip()

def test_case1():
    assert q2.format_solution(q2.solve(8, [0], 4), sep='') == """
00100
01010
00100
00000
00000""".lstrip()

def test_case2():
    assert q2.format_solution(q2.solve(6, [3,5,11], 18), sep='') == """
11110
11121
00111
10010
11001""".lstrip()

def test_case3():
    assert q2.format_solution(q2.solve(12, [1,24], 7), sep='') == """
00000
01100
11010
01100
00000""".lstrip()

def test_case4():
    assert q2.format_solution(q2.solve(7, [2,9,14], 23), sep='') == """
02120
21012
02220
01310
00100""".lstrip()

def test_case5():
    assert q2.format_solution(q2.solve(1, [4,16,4,1], 61), sep='') == """
01133
12003
10000
30003
33033""".lstrip()

def test_case6():
    assert q2.format_solution(q2.solve(18, [2,2,24,23,4], 76), sep='') == """
13331
31213
32323
31313
13331""".lstrip()

def test_case7():
    assert q2.format_solution(q2.solve(3, [2, 3, 5, 7, 11, 13], 150), sep='') == """
23232
32223
22222
32223
23232""".lstrip()

def test_case8():
    assert q2.format_solution(q2.solve(3, [2, 3, 5, 7, 11, 13], 999), sep='') == """
23230
22322
32321
31122
03313""".lstrip()
