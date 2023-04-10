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


class Solution:
    def __init__(self):
        self.coins = []
        self.amount = 0
        self.comboes = []

    def change(self, amount: int, coins: List[int]) -> int:
        self.amount = amount
        self.coins = coins
        self.coins.sort(reverse=True)
        return len(self.comboes)


def main():
    file = open("../data/coin_change_2.txt")
    lines = file.readlines()

    coin_changer = Solution()

    for line in lines:
        amount = line.split



if __name__ == '__main__':
    main()
