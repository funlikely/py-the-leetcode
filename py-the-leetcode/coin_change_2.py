"""
    518. Coin Change II
    Medium
    Companies

    You are given an integer array coins representing coins of different denominations and an integer amount
    representing a total amount of money.

    Return the number of combinations that make up that amount. If that amount of money cannot be made up by any
    combination of the coins, return 0.

    You may assume that you have an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.

    Note: test cases should include,
    1. Primes, with a nonzero result (change can be made). E.g., change(101, [2, 3, 5, 7, 11])
    2. Zero result. E.g., change(100, [51, 52, 54, 55, 56, 66])
    3. A nice long case, like the project euler one that has 72,000 ways of making change.
        E.g., change(200, [200, 100, 50, 20, 10, 5, 2, 1])

"""
from typing import List
import ast


class Solution:
    def __init__(self):
        self.coins = []
        self.amount = 0
        self.combos = []

    def change(self, amount: int, coins: List[int]) -> int:
        self.amount = amount
        self.coins = coins
        self.coins.sort(reverse=True)
        base_coins = {c: 0 for c in coins}

        self.combos = [base_coins]

        for i in range(len(coins)):
            """
                Start of loop: Every coin in coins up to 'i' should be REPRESENTED in self.combos
                Initially: self.combos = [{base_coins}]
            """
            coin_value = coins[i]
            for combo in self.combos:


                new_combos = []

                self.combos = new_combos

        return len(self.combos)


def main():
    file = open("../data/coin_change_2.txt")
    lines = file.readlines()

    coin_changer = Solution()

    for line in lines:
        coin_changer.amount, coin_changer.coins = ast.literal_eval(line)
        change_result = coin_changer.change(coin_changer.amount, coin_changer.coins)
        print(f"Let's change these coins! Amount: {coin_changer.amount}, Coins: {coin_changer.coins}, " +
                f"Ways of change: {change_result}")


if __name__ == '__main__':
    main()
