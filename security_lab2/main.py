def do_xoring(line_x, line_y):
    xored = [line_x[i] ^ (0 if len(line_y) < i + 1 else line_y[i]) for i in range(len(line_x))]
    return bytearray(xored)


def get_the_beginning(raw_lines, lines_count, suspected_text):
    for j in range(lines_count):
        print('New try')

        line_index = j

        likely_wrong = False

        susp_deciphered = {}
        for i in range(lines_count):
            deciphered = do_xoring(do_xoring(raw_lines[line_index], raw_lines[i]),
                                   bytearray.fromhex(''.join(hex(ord(c))[2:] for c in suspected_text)))
            deciphered_text = deciphered[:len(suspected_text)].decode("utf-8")
            print(f'line {i} after xor: {deciphered_text}')
            susp_deciphered[i] = deciphered
            chars = set('#@%^*${}[]+=~/<>\\')
            if any((c in chars) for c in deciphered_text):
                likely_wrong = True

        if not likely_wrong:
            print('\nSaving results\n', '-' * 50)
            for line_number, line in susp_deciphered.items():
                actual_text[line_number] = line[:len(suspected_text)].decode('utf-8')
        else:
            print('\nLikely wrong, results will not be saved\n', '-' * 50)

        print('Result:')
        for line_number, line in actual_text.items():
            print(line_number, ' | ', line)
    return susp_deciphered


if __name__ == '__main__':
    raw_lines = []
    actual_text = {}
    with open('encrypted.txt', 'r') as file:
        for line in file.readlines():
            raw_lines.append(bytearray.fromhex(line))
    print(raw_lines)
    lines_count = len(raw_lines)
    get_the_beginning(raw_lines, lines_count, 'The ')
