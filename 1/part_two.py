def solve(depths_input):
    depths = [int(i) for i in depths_input.split()]
    counter = 0
    for i in range(len(depths) - 3):
        if sum(depths[i + 1 : i + 4]) > sum(depths[i : i + 3]):
            counter += 1
    return counter


if __name__ == "__main__":
    with open("input.txt") as f:
        txt_input = f.read()
    print(solve(txt_input))
