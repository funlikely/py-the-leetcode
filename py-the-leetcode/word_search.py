"""
    Word Search
    https://leetcode.com/problems/word-search/

"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return True


def get_word(line):
    return "ASDF"


def get_board(line):
    return [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]


def main():
    file = open("../data/word_search.txt")
    lines = file.readlines()

    word_check = Solution()

    for line in lines:
        word = get_word(line)
        board = get_board(line)

        exists = word_check.exist(board, word)

        print(f"Existence of word '{word}': {exists}")

    # word = "ASDF"
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]


if __name__ == '__main__':
    main()
