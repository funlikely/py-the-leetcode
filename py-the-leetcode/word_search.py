"""
    Word Search
    https://leetcode.com/problems/word-search/

"""
from typing import List
from ast import literal_eval


class Solution:
    def __init__(self):
        self.board = []
        self.n = 0  # width
        self.m = 0  # height
        self.vert_directions = {0: -1, 1: 0, 2: 1, 3: 0}
        self.horiz_directions = {0: 0, 1: 1, 2: 0, 3: -1}

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.m = len(board)  # height
        self.n = len(board[0])  # width
        if not self.quick_tests_pass(word):
            return False
        for i in range(self.n):
            for j in range(self.m):
                if board[j][i] == word[0]:
                    if self.exist_recursive(word, (j, i), [(j, i)]):
                        return True
        return False

    def exist_recursive_direction(self, word, j, i, direction, used_indices):
        next_coord = (j + self.vert_directions[direction], i + self.horiz_directions[direction])

        if next_coord[0] == -1 or next_coord[0] == self.m or next_coord[1] == -1 or next_coord[1] == self.n:
            return False
        if self.board[next_coord[0]][next_coord[1]] != word[0] or next_coord in used_indices:
            return False
        more_used_indices = [next_coord] + used_indices
        return self.exist_recursive(word, next_coord, more_used_indices)

    def exist_recursive(self, word, start_coord, used_indices):
        if len(word) == 0:
            print(f"found the word, used_indices: {used_indices[::-1]}")
            return True
        j, i = start_coord
        if len(word) == 1 and self.board[j][i] == word[0]:
            print(f"found the word, used_indices: {used_indices[::-1]}")
            return True
        if not self.exist_recursive_direction(word[1:], j, i, 0, used_indices):
            if not self.exist_recursive_direction(word[1:], j, i, 1, used_indices):
                if not self.exist_recursive_direction(word[1:], j, i, 2, used_indices):
                    if not self.exist_recursive_direction(word[1:], j, i, 3, used_indices):
                        return False
        return True

    def quick_tests_pass(self, word):
        board_letter_list = [letter for row in self.board for letter in row]
        if len([word_letter for word_letter in word if word_letter not in board_letter_list]):
            return False
        if len(word) > len(board_letter_list):
            return False
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
        print(f"word: {word}, board: {board}")

        exists = word_check.exist(board, word)

        print(f"Existence of word '{word}': {exists}")

    # word = "ASDF"
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]


if __name__ == '__main__':
    main()
