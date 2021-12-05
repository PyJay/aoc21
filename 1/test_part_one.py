from part_one import solve


def test_example():
    test_input = """
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
    """
    assert 7 == solve(test_input)
