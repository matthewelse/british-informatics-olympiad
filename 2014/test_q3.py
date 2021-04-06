import q3


def test_example():
    assert q3.solve(37) == "AB"


def test_case0():
    assert q3.solve(1) == "A"


def test_case1():
    assert q3.solve(21) == "U"


def test_case2():
    assert q3.solve(321) == "JP"


def test_case3():
    assert q3.solve(4321) == "HPQ"


def test_case4():
    assert q3.solve(54321) == "LNOV"


def test_case5():
    assert q3.solve(654321) == "AHJSVW"


def test_case6():
    assert q3.solve(7654321) == "EHJK025"


def test_case7():
    assert q3.solve(87654321) == "CEILRU059"


def test_case8():
    assert q3.solve(234234234) == "BEHJPVX267"


def test_case9():
    assert q3.solve(987654321) == "MNOPQTUX026"

