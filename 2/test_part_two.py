from part_two import solve

def test_part_two():
    with open('test_input.txt') as f:
        input_lines = f.readlines()
    assert 900 == solve(input_lines)