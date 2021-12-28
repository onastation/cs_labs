def search_for_keys(cipher):
    for k in range(258):
        res = "".join([chr(c ^ k) for c in cipher])
        print(k, res)


def run_task1(single_byte_xor_cipher):
    print('TASK 1\nCiphered data:\n', single_byte_xor_cipher)
    print('Finding the key:\n')
    search_for_keys(single_byte_xor_cipher)
    k = 23
    print('Deciphering and cleaning:')

    single_byte_xor_result = "".join([chr(c ^ k) for c in single_byte_xor_cipher])
    for c in single_byte_xor_result:
        if not c.isalnum():
            # print(c, '----', bytes(c, encoding='utf-8'))
            single_byte_xor_result = single_byte_xor_result.replace(c, ' ')
    print(single_byte_xor_result)
    single_byte_xor_result = single_byte_xor_result.replace('Â', '')
    single_byte_xor_result = single_byte_xor_result.replace('¼', '')
    single_byte_xor_result = single_byte_xor_result.replace('½', '')
    print('Result:\n', single_byte_xor_result)
