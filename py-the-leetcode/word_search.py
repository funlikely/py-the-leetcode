"""
    Word Search
    https://leetcode.com/problems/word-search/

"""
from typing import List
from ast import literal_eval


class Solution:
    def __init__(self):
        self.board = []
        self.n = 0
        self.m = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.n = len(board)  # height
        self.m = len(board[0])  # length
        for i in range(self.m):
            for j in range(self.n):
                if board[j][i] == word[0]:
                    if self.exist_recursive(word, (j, i), []):
                        return True
        return False

    def exist_recursive_right(self, word, start_coord, used_indices):
        j, i = start_coord
        if i == self.m - 1 or self.board[j][i + 1] != word[0] or start_coord in used_indices:
            return False
        return self.exist_recursive(word[1:], (j, i + 1), used_indices.append(start_coord))

    def exist_recursive_left(self, word, start_coord, used_indices):
        j, i = start_coord
        if i == 0 or self.board[j][i - 1] != word[0] or start_coord in used_indices:
            return False
        return self.exist_recursive(word[1:], (j, i - 1), used_indices.append(start_coord))

    def exist_recursive_up(self, word, start_coord, used_indices):
        j, i = start_coord
        if j == 0 or self.board[j - 1][i] != word[0] or start_coord in used_indices:
            return False
        return self.exist_recursive(word[1:], (j - 1, i), used_indices.append(start_coord))

    def exist_recursive_down(self, word, start_coord, used_indices):
        j, i = start_coord
        if j == self.m - 1 or self.board[j + 1][i] != word[0] or start_coord in used_indices:
            return False
        return self.exist_recursive(word[1:], (j + 1, i), used_indices.append(start_coord))

    def exist_recursive(self, word, start_coord, used_indices):
        if len(word) == 0:
            print(f"found the word, used_indices: {used_indices.append(start_coord)}")
            return True
        return self.exist_recursive_up(word, start_coord, used_indices) or \
            self.exist_recursive_down(word, start_coord, used_indices) or \
            self.exist_recursive_right(word, start_coord, used_indices) or \
            self.exist_recursive_left(word, start_coord, used_indices)


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
