#!/usr/bin/python3
""" Prime Game """


def is_prime(num):
    """ Function that determines if a number is a prime number"""

    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def take_turn(valid_numbers):
    """ Function that regulates a players pick per every turn """

    valid_picks = [num for num in valid_numbers]
    if not valid_picks:
        return None
    pick = valid_picks.pop(0)
    return pick


def prime_game(n):
    """ Function that returns a winner per game """

    numbers = list(range(1, n + 1))
    prime_n = []
    for num in numbers:
        if is_prime(num):
            prime_n.append(num)
    Maria_move = 0
    Ben_move = 0

    while prime_n:

        Maria_move += 1
        Maria_pick = take_turn(prime_n)
        if Maria_pick is not None:
            prime_n.remove(Maria_pick)
        else:
            break

        if prime_n:
            Ben_move += 1
            Ben_pick = take_turn(prime_n)
            if Ben_pick is not None:
                prime_n.remove(Ben_pick)
            else:
                break

    if Maria_move > Ben_move:
        return 'Maria'
    elif Ben_move > Maria_move or Maria_move == Ben_move:
        return 'Ben'


def isWinner(x, nums):
    """ Function that returns the player with most wins """

    if x is None or x <= 0:
        return None

    if nums == []:
        return None

    array_n = [i for i in nums]
    if x != len(array_n):
        return None
    winner = []
    for n in array_n:
        curr_win = prime_game(n)
        winner.append(curr_win)
    return (max(winner, key=winner.count))
