from collections import Counter


def calculate_power_consumption(input_str):
    vertical_lists = get_vertical_lists(input_str)
    counters = []
    for l in vertical_lists:
        counters.append(Counter(l))
    gamma_bits = [0 if c[0] > c[1] else 1 for c in counters]
    epsilon_bits = [0 if c[0] < c[1] else 1 for c in counters]
    gamma_str = "".join((str(b) for b in gamma_bits))
    epsilon_str = "".join((str(b) for b in epsilon_bits))
    gamma_decimal = int(gamma_str, 2)
    epsilon_decimal = int(epsilon_str, 2)
    return gamma_decimal * epsilon_decimal


def get_vertical_lists(input_str):
    int_lists = [[int(s) for s in list(i)] for i in input_str]
    vertical_lists = []
    # assume all list lengths are equal and use first one
    list_len = len(int_lists[0])
    for i in range(list_len):
        vertical_lists.append([])
        for l in int_lists:
            vertical_lists[i].append(l[i])
    return vertical_lists


if __name__ == "__main__":
    with open("actual_input.txt") as f:
        input_text = f.readlines()
    input_text = [t.strip() for t in input_text]
    print(calculate_power_consumption(input_text))

