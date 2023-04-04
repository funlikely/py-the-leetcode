"""
    Word Search
    https://leetcode.com/problems/word-search/

"""
from typing import List
from ast import literal_eval


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return True


def get_word(line):
    return literal_eval(line.split(' ')[5])


def get_board(line):
    return literal_eval(line.split(' ')[2].strip(','))


def main():
    file = open("../data/word_search.txt")
    lines = file.readlines()

    word_check = Solution()

    for line in lines:
        word = get_word(line)
        board = get_board(line)
        print(f"word: {word}, board:{board}")

        exists = word_check.exist(board, word)

        print(f"Existence of word '{word}': {exists}")

    # word = "ASDF"
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]


if __name__ == '__main__':
    main()
