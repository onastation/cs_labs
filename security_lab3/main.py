import random
import requests
from crackers import crack_mt, crack_lcg, get_lcg_generator
from mersenne_twister import MT19937


def createacc(player_id):
    game_params = {'id': player_id}
    req = requests.get('http://95.217.177.249/casino/createacc', game_params)
    return req.json()


def play(mode, player_id, amount_of_money, num_to_bet_on):
    url = f'http://95.217.177.249/casino/play{mode}'
    game_params = {
        'id': player_id['id'],
        'bet': amount_of_money,
        'number': num_to_bet_on
    }
    req = requests.get(url, game_params)
    return req.json()


def place_bets(mode, player, num, bet=1):
    nums = list()
    for i in range(num):
        res = play(mode, player, bet, 0)
        player = res['account']
        nums.append(int(res["realNumber"]))
    return player, nums


def win(mode, player_id, bet_num, gen):
    return play(mode, player_id, bet_num, next(gen))


if __name__ == '__main__':
    new_acc = createacc(random.randrange(2 ** 32))
    while 'error' in new_acc:
        new_acc = createacc(random.randrange(2 ** 32))
    player = new_acc
    print('LCG:')
    player, nums = place_bets('Lcg', player, 20)
    args = crack_lcg(nums, 2 ** 33, 2 ** 32)
    state = get_lcg_generator(nums[-1], args[0], args[1], args[2])
    result = win('Lcg', player, 100, state)
    print(result['message'])

    print('Mersenne Twister:')
    player, nums = place_bets('Mt', player, MT19937.n)
    state = crack_mt(nums).get_mt_generator()
    result = win('Mt', player, 100, state)
    print(result['message'])

    print('Better Mersenne Twister:')
    player, nums = place_bets('BetterMt', player, MT19937.n)
    state = crack_mt(nums).get_mt_generator()
    result = win('Mt', player, 100, state)
    print(result['message'])
