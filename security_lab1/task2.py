import base64
import numpy as np
import plotly.express as px


def coincidence_estimation(cipher):
    coincidences = {}
    for i in range(1, len(cipher)):
        shifted_ciphertext = cipher[-i:] + cipher[:-i]
        coincidences[i] = sum(list(
            map(lambda x: x[0] == x[1], zip(cipher, shifted_ciphertext))
        ))

    return coincidences


MAX_KEY_LENGTH_GUESS = 20
alphabet = 'abcdefghijklmnopqrstuvwxyz'

english_frequences = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                      0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                      0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                      0.00978, 0.02360, 0.00150, 0.01974, 0.00074]


def freq_analysis(sequence):
    all_chi_squareds = [0] * 26

    for i in range(26):

        chi_squared_sum = 0.0
        sequence_offset = [chr(((ord(sequence[j]) - 97 - i) % 26) + 97) for j in range(len(sequence))]
        v = [0] * 26
        for l in sequence_offset:
            v[ord(l) - ord('a')] += 1
        for j in range(26):
            v[j] *= (1.0 / float(len(sequence)))

        for j in range(26):
            chi_squared_sum += ((v[j] - float(english_frequences[j])) ** 2) / float(english_frequences[j])

        all_chi_squareds[i] = chi_squared_sum

    shift = all_chi_squareds.index(min(all_chi_squareds))

    return chr(shift + 97)


def get_key(ciphertext, key_length):
    key = ''
    for i in range(key_length):
        sequence = ""
        for j in range(0, len(ciphertext[i:]), key_length):
            sequence += ciphertext[i + j]
        key += freq_analysis(sequence)

    return key


def decrypt(ciphertext, key):
    cipher_ascii = [ord(letter) for letter in ciphertext]
    key_ascii = [ord(letter) for letter in key]
    plain_ascii = []

    for i in range(len(cipher_ascii)):
        plain_ascii.append(((cipher_ascii[i] - key_ascii[i % len(key)]) % 26) + 97)

    plaintext = ''.join(chr(i) for i in plain_ascii)
    return plaintext


def run_task2(vigenere_cipher):
    print('TASK 2')

    print(vigenere_cipher)
    coincidences = coincidence_estimation(vigenere_cipher)
    fig = px.line(x=coincidences.keys(), y=coincidences.values(), markers=True)
    fig.update_layout(xaxis_range=[0, 20])
    fig.show()

    ciphertext = ''.join(str(x).lower() for x in vigenere_cipher if str(x).isalpha())

    key_length = 3
    print("Key length is {}".format(key_length))

    key = get_key(ciphertext, key_length)
    plaintext = decrypt(ciphertext, key)

    print("Key: {}".format(key))
    print("Plaintext: {}".format(plaintext))
