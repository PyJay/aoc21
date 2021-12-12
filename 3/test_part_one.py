from part_one import calculate_power_consumption

def test_part_one():
    with open("test_input.txt") as f:
        input_text = f.readlines()
    input_text = [t.strip() for t in input_text]
    assert 198 == calculate_power_consumption(input_text)

