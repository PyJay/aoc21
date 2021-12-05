from part_one import solve

def test_part_one():
    with open('test_input.txt') as f:
        input_lines = f.readlines()
    assert 150 == solve(input_lines)