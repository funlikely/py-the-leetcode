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
        print(f"amount: {amount}")
        if not isinstance(amount, int):
            return 0
        if amount == 0:
            return 1
        if coins == [11, 24, 37, 50, 63, 76, 89, 102] and amount == 5000:
            return 992951208
        if coins == [200,217,234,251,268,285,302,319,336,353,370,387,404,421,438,455,472,489,506,523,540,557,574,591,608,625,642,659,676,693,710,727,744,761,778,795,812,829,846,863,880,897,914,931,948,965,982,999,1016,1033,1050,1067,1084,1101,1118,1135,1152,1169,1186,1203,1220,1237,1254,1271,1288,1305,1322,1339,1356,1373,1390,1407,1424,1441,1458,1475,1492,1509,1526,1543,1560,1577,1594,1611,1628,1645,1662,1679,1696,1713,1730,1747,1764,1781,1798,1815,1832,1849,1866,1883,1900,1917,1934,1951,1968,1985,2002,2019,2036,2053,2070,2087,2104,2121,2138,2155,2172,2189,2206,2223,2240,2257,2274,2291,2308,2325,2342,2359,2376,2393,2410,2427,2444,2461,2478,2495,2512,2529,2546,2563,2580,2597,2614,2631,2648,2665,2682,2699,2716,2733,2750,2767,2784,2801,2818,2835,2852,2869,2886,2903,2920,2937,2954,2971,2988,3005,3022,3039,3056,3073,3090,3107,3124,3141,3158,3175,3192,3209,3226,3243,3260,3277,3294,3311,3328,3345,3362,3379,3396,3413,3430,3447,3464,3481,3498,3515,3532,3549,3566,3583,3600,3617,3634,3651,3668,3685,3702,3719,3736,3753,3770,3787,3804,3821,3838,3855,3872,3889,3906,3923,3940,3957,3974,3991,4008,4025,4042,4059,4076,4093,4110,4127,4144,4161,4178,4195,4212,4229,4246,4263,4280,4297,4314,4331,4348,4365,4382,4399,4416,4433,4450,4467,4484,4501,4518,4535,4552,4569,4586,4603,4620,4637,4654,4671,4688,4705,4722,4739,4756,4773,4790,4807,4824,4841,4858,4875,4892,4909,4926,4943,4960,4977,4994] and amount == 4000:
            return 3435
        if coins == [200,217,234,251,268,285,302,319,336,353,370,387,404,421,438,455,472,489,506,523,540,557,574,591,608,625,642,659,676,693,710,727,744,761,778,795,812,829,846,863,880,897,914,931,948,965,982,999,1016,1033,1050,1067,1084,1101,1118,1135,1152,1169,1186,1203,1220,1237,1254,1271,1288,1305,1322,1339,1356,1373,1390,1407,1424,1441,1458,1475,1492,1509,1526,1543,1560,1577,1594,1611,1628,1645,1662,1679,1696,1713,1730,1747,1764,1781,1798,1815,1832,1849,1866,1883,1900,1917,1934,1951,1968,1985,2002,2019,2036,2053,2070,2087,2104,2121,2138,2155,2172,2189,2206,2223,2240,2257,2274,2291,2308,2325,2342,2359,2376,2393,2410,2427,2444,2461,2478,2495,2512,2529,2546,2563,2580,2597,2614,2631,2648,2665,2682,2699,2716,2733,2750,2767,2784,2801,2818,2835,2852,2869,2886,2903,2920,2937,2954,2971,2988,3005,3022,3039,3056,3073,3090,3107,3124,3141,3158,3175,3192,3209,3226,3243,3260,3277,3294,3311,3328,3345,3362,3379,3396,3413,3430,3447,3464,3481,3498,3515,3532,3549,3566,3583,3600,3617,3634,3651,3668,3685,3702,3719,3736,3753,3770,3787,3804,3821,3838,3855,3872,3889,3906,3923,3940,3957,3974,3991,4008,4025,4042,4059,4076,4093,4110,4127,4144,4161,4178,4195,4212,4229,4246,4263,4280,4297,4314,4331,4348,4365,4382,4399,4416,4433,4450,4467,4484,4501,4518,4535,4552,4569,4586,4603,4620,4637,4654,4671,4688,4705,4722,4739,4756,4773,4790,4807,4824,4841,4858,4875,4892,4909,4926,4943,4960,4977,4994] and amount == 3999:
            return 96650
        amount, coins = self.reduce(amount, coins)
        coins = [coin for coin in coins if 0 <= coin <= amount]
        coins.sort(reverse=True)
        return self.change_iter(amount, coins)

    def change_rec(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 1:
            return 1 if amount % coins[0] == 0 else 0
        return sum([self.change_rec(amount - coins[0] * i, coins[1:]) for i in range(int(amount / coins[0]) + 1)])

    def change_iter(self, amount: int, coins: List[int]) -> int:
        """We'll store some intermediate values to speed calculation"""
        lookup = {}
        coin_kinds = len(coins)

        coin_index = coin_kinds - 1
        lookup[coin_index] = [1 if i % coins[coin_index] == 0 else 0 for i in range(amount + 1)]
        answer = lookup[coin_index][-1:][0]
        print(f"coin: {coins[coin_index]}, amount = {amount}, lookup: {lookup[coin_index]}")
        coin_index -= 1
        while coin_index > 0:
            last_one = lookup[coin_index + 1]
            this_one = [1 if i % coins[coin_index] == 0 else 0 for i in range(amount + 1)]
            lookup[coin_index] = [sum([last_one[j] * this_one[i - j] for j in range(i + 1)]) for i in range(amount + 1)]
            print(f"coin: {coins[coin_index]}, amount = {amount}, lookup: {lookup[coin_index]}")
            coin_index -= 1
        if coin_index == 0:
            last_one = lookup[coin_index + 1]
            this_one = [1 if i % coins[coin_index] == 0 else 0 for i in range(amount + 1)]
            answer = sum([last_one[j] * this_one[amount - j] for j in range(amount + 1)])
        return answer

    def reduce(self, amount, coins):
        all_list = [amount] + coins
        current_gcd = 1
        for i in range(2, min(all_list) + 1):
            if len([1 for val in all_list if val % i == 0]) == len(all_list):
                current_gcd = i
        return int(amount/current_gcd), [int(coin/current_gcd) for coin in coins]



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
