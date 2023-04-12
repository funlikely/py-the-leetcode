"""
    518. Coin Change II

    https://leetcode.com/problems/coin-change-ii/

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
    3. A nice long case, like the project euler one that has 73682 ways of making change.
        E.g., change(200, [200, 100, 50, 20, 10, 5, 2, 1])

"""
from typing import List
import ast


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        return self.change_iter(amount, coins)

    def change_rec(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 1:
            return 1 if amount % coins[0] == 0 else 0
        return sum([self.change_rec(amount - coins[0] * i, coins[1:]) for i in range(int(amount / coins[0]) + 1)])

    def change_iter(self, amount: int, coins: List[int]) -> int:
        """We'll store some intermediate values to speed calculation"""
        change_count = 0
        lookup = {}
        coin_kinds = len(coins)

        coin_index = coin_kinds - 1
        lookup[coin_index] = [1 if i % coins[coin_index] == 0 else 0 for i in range(amount + 1)]
        print(f"coin: {coins[coin_index]}, amount = {amount}, lookup: {lookup[coin_index]}")
        coin_index -= 1
        while coin_index >= 0:
            last_one = lookup[coin_index + 1]
            this_one = [1 if i % coins[coin_index] == 0 else 0 for i in range(amount + 1)]
            lookup[coin_index] = [sum([last_one[j] * this_one[i-j] for j in range(i+1)]) for i in range(amount + 1)]
            print(f"coin: {coins[coin_index]}, amount = {amount}, lookup: {lookup[coin_index]}")
            coin_index -= 1
        return lookup[0][-1:][0]


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
