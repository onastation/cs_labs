from math import fmod
from mersenne_twister import MT19937, un_bitshift_left_xor, un_bitshift_right_xor


def get_mt_state(num):
    num = un_bitshift_right_xor(num, MT19937.l)
    num = un_bitshift_left_xor(num, MT19937.t, mask=MT19937.c)
    num = un_bitshift_left_xor(num, MT19937.s, mask=MT19937.b)
    num = un_bitshift_right_xor(num, MT19937.u, mask=MT19937.d)
    return num

def crack_mt(nums):
    nums = nums[:MT19937.n]
    mt_state = list()
    for num in nums:
        mt_state.append(get_mt_state(num))

    return MT19937(state=mt_state)


def get_c(x, nxt, a, m):
    multm = (a * x) % m
    left = m - multm
    c = (left + nxt) % m
    return c


def calculate_difference(i, nums, m):
    d = nums[i + 1] - nums[i]
    if d < 0:
        d += m
    return d


def get_lcg_generator(nums, a, c, m):
    previous = nums
    while True:
        val = a * previous + c
        curr = fmod((val + 2 ** 31) % 2 ** 32 - 2 ** 31, m)
        yield int(curr)
        previous = curr


def crack_lcg(nums, max_mod, min_mod):
    for m in range(min_mod, max_mod):
        d = list()
        for i in range(0, len(nums) - 1):
            d.append(calculate_difference(i, nums, m))
        try:
            invrs = pow(d[0], -1, m)
        except ValueError:
            continue
        a = (d[1] * invrs) % m
        obs_diffs = [(a * diff) % m for diff in d]
        if d[1:] == obs_diffs[:-1]:
            c = get_c(nums[0], nums[1], a, m)
            return a, c, m
