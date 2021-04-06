import q1

def test_cases():
    cases = [
        (5, (3, 7)),
        (33, (31, 37)),
        (34, (33, 37)),
        (399, (393, 409)),
        (456, (451, 463)),
        (3301, (3297, 3307)),
        (3304, (3301, 3307)),
        (9703, (9691, 9727)),
        (10000, (9999, 10003)),
    ]

    for (problem, expected) in cases:
        result = q1.solve(problem)

        assert result == expected
