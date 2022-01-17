import random
import string

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + '1234567890/?.,!@*%' * 3


def generate_random_password(min_length=6, max_length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(random.randint(min_length, max_length)))
    return password


def generate_human_password(words_pool, min_words, max_words):
    amount = random.randint(min_words, max_words)
    password = ''.join(random.choice(words_pool) for i in range(amount)).lower()
    password = ''.join(char if random.choice((True, False)) else char.upper() for char in password)
    if random.choice((True, False)):
        password += str(random.randint(0, 100))
    else:
        if random.choice((True, False)):
            password += str(random.randint(1960, 2021))

    return password
