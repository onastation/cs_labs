def do_xoring(line_x, line_y):
    xored = [line_x[i] ^ (0 if len(line_y) < i + 1 else line_y[i]) for i in range(len(line_x))]
    return bytearray(xored)


def check_text(raw_lines, lines_count, actual_text, suspected_text):
    for j in range(lines_count):
        print('-' * 50, '\nNew try')

        line_index = j

        likely_wrong = False

        suspected_deciphered = {}
        for i in range(lines_count):
            deciphered = do_xoring(do_xoring(raw_lines[line_index], raw_lines[i]),
                                   bytearray.fromhex(''.join(hex(ord(c))[2:] for c in suspected_text)))
            deciphered_text = deciphered[:len(suspected_text)].decode("utf-8")
            print('result text: ', deciphered_text)
            suspected_deciphered[i] = deciphered
            chars = set('#@%^*${}[]+=~/<>\\')
            if any((c in chars) for c in deciphered_text):
                likely_wrong = True

        if not likely_wrong:
            print('\nSaving results\n')
            for line_number, line in suspected_deciphered.items():
                actual_text[line_number] = line[:len(suspected_text)].decode('utf-8')
        else:
            print('\nLikely wrong, results will not be saved\n')

        print('Actual text:')
        for line_number, line in actual_text.items():
            print(line)


if __name__ == '__main__':
    raw_lines = []
    actual_text = {}
    with open('encrypted.txt', 'r') as file:
        for line in file.readlines():
            raw_lines.append(bytearray.fromhex(line))
    print(raw_lines)
    lines_count = len(raw_lines)
    #check_text(raw_lines, lines_count, 'The ')
    while True:
        new_text = input("Input new text to check: ")
        check_text(raw_lines, lines_count, actual_text, new_text)
