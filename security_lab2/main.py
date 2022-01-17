def do_xoring(line_x, line_y):
    xored = [line_x[i] ^ (line_y[i] if len(line_y) >= i else 0) for i in range(len(line_x))]
    return bytearray(xored)


if __name__ == '__main__':
    raw_lines = []
    actual_text = {}
    with open('encrypted.txt', 'r') as file:
        for line in file.readlines():
            raw_lines.append(bytearray.fromhex(line))

    print(raw_lines)

    lines_count = len(raw_lines)
