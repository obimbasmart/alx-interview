#!/usr/bin/python3


"""Solve Prime Game
"""


def isWinner(x, nums):
    def get_primes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(n + 1) if primes[i]]

    def play_game(n):
        primes = get_primes(n)
        maria_turn = True
        while primes:
            next_prime = primes.pop(0)
            primes = [p for p in primes if p % next_prime != 0]
            maria_turn = not maria_turn
        return "Maria" if not maria_turn else "Ben"

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
