def do_xoring(line_x, line_y):
    xored = [line_x[i] ^ (line_y[i] if len(line_y) >= i else 0) for i in range(len(line_x))]
    return bytearray(xored)
