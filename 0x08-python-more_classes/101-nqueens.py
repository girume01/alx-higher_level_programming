#!/usr/bin/python3
""" solves the nqueens puzzle"""

import sys

class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def get_solution(self):
        solution = []
        for r in range(self.n):
            for c in range(self.n):
                if self.board[r][c] == "Q":
                    solution.append([r, c])
                    break
        return solution

    def xout(self, row, col):
        for c in range(col + 1, self.n):
            self.board[row][c] = "x"
        for c in range(col - 1, -1, -1):
            self.board[row][c] = "x"
        for r in range(row + 1, self.n):
            self.board[r][col] = "x"
        for r in range(row - 1, -1, -1):
            self.board[r][col] = "x"
        c = col + 1
        for r in range(row + 1, self.n):
            if c >= self.n:
                break
            self.board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            self.board[r][c] = "x"
            c -= 1
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c >= self.n:
                break
            self.board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row + 1, self.n):
            if c < 0:
                break
            self.board[r][c] = "x"
            c -= 1

    def recursive_solve(self, row, queens):
        if queens == self.n:
            self.solutions.append(self.get_solution())
            return

        for c in range(self.n):
            if self.board[row][c] == " ":
                tmp_board = [row[:] for row in self.board]
                tmp_board[row][c] = "Q"
                self.xout(row, c)
                self.recursive_solve(row + 1, queens + 1)

    def solve_nqueens(self):
        self.recursive_solve(0, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(n)
    solver.solve_nqueens()
    for sol in solver.solutions:
        print(sol)

