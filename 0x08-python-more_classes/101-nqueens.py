#!/usr/bin/python3
"""
A module: To solve the NQueen Puzzle
"""

import sys


def init_board(n):
    """Initialize an empty chessboard of size n x n."""
    return [[' ' for _ in range(n)] for _ in range(n)]


def get_queen_positions(board):
    """Get the positions of queens on the board."""
    return [[row, col] for row in range(
        len(board)) for col in range(len(board)) if board[row][col] == "Q"]


def mark_attacked_cells(board, row, col):
    """Mark cells attacked by a queen at position (row, col)."""
    for current_col in range(col + 1, len(board)):
        board[row][current_col] = "x"
    for current_col in range(col - 1, -1, -1):
        board[row][current_col] = "x"
    for current_row in range(row + 1, len(board)):
        board[current_row][col] = "x"
    for current_row in range(row - 1, -1, -1):
        board[current_row][col] = "x"
    current_col, current_row = col + 1, row + 1
    while current_col < len(board) and current_row < len(board):
        board[current_row][current_col] = "x"
        current_col += 1
        current_row += 1
    current_col, current_row = col - 1, row - 1
    while current_col >= 0 and current_row >= 0:
        board[current_row][current_col] = "x"
        current_col -= 1
        current_row -= 1
    current_col, current_row = col + 1, row - 1
    while current_col < len(board) and current_row >= 0:
        board[current_row][current_col] = "x"
        current_col += 1
        current_row -= 1
    current_col, current_row = col - 1, row + 1
    while current_col >= 0 and current_row < len(board):
        board[current_row][current_col] = "x"
        current_col -= 1
        current_row += 1


def solve_n_queens(board, current_row, queens_placed, solutions):
    """Recursively solve the N-Queens problem."""
    if queens_placed == len(board):
        solutions.append(get_queen_positions(board))
        return solutions

    for current_col in range(len(board)):
        if board[current_row][current_col] == " ":
            new_board = [row.copy() for row in board]
            new_board[current_row][current_col] = "Q"
            mark_attacked_cells(new_board, current_row, current_col)
            solutions = solve_n_queens(
                    new_board, current_row + 1, queens_placed + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    chessboard = init_board(n)
    solutions = solve_n_queens(chessboard, 0, 0, [])
    for solution in solutions:
        print(solution)
