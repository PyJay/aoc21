def solve(depths_input):
    depths = [int(i) for i in depths_input.split()]
    counter = 0
    for i in range(len(depths) - 1):
        if depths[i + 1] > depths[i]:
            counter += 1
    return counter


if __name__ == "__main__":
    with open("input.txt") as f:
        txt_input = f.read()
    print(solve(txt_input))
