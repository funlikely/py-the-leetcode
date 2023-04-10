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
"""
from typing import List


class Solution:
    def __init__(self):
        self.coins = []
        self.amount = 0
        self.comboes = []

    def change(self, amount: int, coins: List[int]) -> int:
        return len(self.comboes)


def main():
    file = open("../data/word_search.txt")
    lines = file.readlines()

    word_check = Solution()

    for line in lines:
        word = get_word(line)
        board = get_board(line)
        print(f"word: {word}, board: {board}")

        exists = word_check.exist(board, word)

        print(f"Existence of word '{word}': {exists}")

    # word = "ASDF"
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]


if __name__ == '__main__':
    main()
