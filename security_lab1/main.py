import binascii
import base64
from pathlib import Path
import numpy as np
import plotly.express as px
from task1 import run_task1
from task2 import run_task2


def decode_intro(filename):
    intro = open(filename, "r", encoding='utf-8').readlines()[0]
    intro = int(intro, 2)
    intro = binascii.unhexlify('%x' % intro)
    intro = base64.b64decode(intro)
    intro = intro.decode("utf-8")
    result = open(Path(filename).stem + '_decoded.txt', "w")
    result.write(intro)
    result.close()
    return intro





if __name__ == '__main__':
    intro = decode_intro('intro.txt')
    intro_lines = intro.split('\n')
    line_counter = 0
    for i in intro_lines:
        print(line_counter, i)
        line_counter += 1


    # TASK 1
    single_byte_xor_cipher = binascii.unhexlify(intro_lines[5])
    run_task1(single_byte_xor_cipher)

    # TASK 2
    vigenere_cipher = base64.b64decode(intro_lines[6])
    print(vigenere_cipher)
    run_task2(vigenere_cipher)

    # TASK 3
    substitution_cipher = intro_lines[7]

