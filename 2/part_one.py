
def solve(input_lines):
    x = 0
    y = 0
    for line in input_lines:
        direction, magnitude_str = line.split()
        magnitude = int(magnitude_str)
        if direction.lower() == 'forward':
            x += magnitude
        if direction.lower() == 'up':
            # up reduces depth by magnitude
            y -= magnitude
        if direction.lower() == 'down':
            y += magnitude
    return x * y


if __name__ == '__main__':
    with open('part_one_input.txt') as f:
        input_lines = f.readlines()
    print(solve(input_lines))