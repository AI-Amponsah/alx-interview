#!/usr/bin/python3
def is_winner(x, nums):
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(limit**0.5) + 1):
            if primes[i]:
                for j in range(i * i, limit + 1, i):
                    primes[j] = False

        return [num for num, is_prime in enumerate(primes) if is_prime]

    def play_game(n):
        primes = sieve_of_eratosthenes(n)
        remaining_numbers = set(range(1, n + 1))

        while remaining_numbers:
            move = None
            for prime in primes:
                if prime in remaining_numbers:
                    move = prime
                    break

            if move is None:
                break

            remaining_numbers -= set(range(move, n + 1, move))

        return "Maria" if len(remaining_numbers) % 2 == 1 else "Ben"

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        winner = play_game(n)
        if winner:
            wins[winner] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
result = is_winner(x, nums)
print(result)
