import random
from generators import generate_random_password, generate_human_password
import hashing_algorithms

if __name__ == '__main__':
    num = 1000
    count = 0
    with open('data/top_hundred.txt') as f:
        hundred_passwords = tuple(line.strip() for line in f)
    with open('data/top_million.txt') as f:
        million_passwords = tuple(line.strip() for line in f)

    passwords = []

    for j in range(num):
        if random.randint(1, 100) in range(1, 6):
            count += 1
            print(count, 'generate random password')
            passwords.append(
                generate_random_password()
            )
        elif random.randint(1, 100) in range(1, 11):
            count += 1
            print(count, 'hundred passwords list')
            passwords.append(
                random.choice(hundred_passwords)
            )
        elif random.randint(1, 100) in range(1, 91):
            count += 1
            print(count, 'million passwords list')
            passwords.append(
                random.choice(million_passwords)
            )
        else:
            count += 1
            print(count, 'human passwords list')
            passwords.append(
                generate_human_password('data/words.txt', 1, 3)
            )
    print(passwords[:50])
    with open('generated_passwords/argon2i_passwords.csv', "w") as csv_file:
        for pswd in hashing_algorithms.create_argon2i_passwords(passwords[:int(num * 0.2)]):
            csv_file.write(f'{pswd}\n')
    with open('generated_passwords/md5_passwords.csv', "w") as csv_file:
        for pswd in hashing_algorithms.create_argon2i_passwords(passwords[int(num * 0.2):int(num * 0.6)]):
            csv_file.write(f'{pswd}\n')
    with open('generated_passwords/sha1_passwords.csv', "w") as csv_file:
        for pswd in hashing_algorithms.create_argon2i_passwords(passwords[int(num * 0.6):]):
            csv_file.write(f'{pswd}\n')
