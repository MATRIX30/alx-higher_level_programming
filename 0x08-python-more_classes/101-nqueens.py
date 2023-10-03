#!/usr/bin/python3
"""program to play N Queen challenge"""


import sys


def is_valid_position(board, row, col):
    """
    Checks if the given position is valid for placing a queen.

    Args:
        board: A list of lists representing the chessboard.
        row: The row index of the position.
        col: The column index of the position.

    Returns:
        True if the position is valid, False otherwise.
    """

    # Check if there is a queen in the same row or column.
    for i in range(len(board)):
        if board[i][col] == 1 or board[row][i] == 1:
            return False

    # Check if there is a queen in a diagonal position.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if abs(i - row) == abs(j - col) and board[i][j] == 1:
                return False

    return True


def solve_n_queens(board, row):
    """
    Solves the N-queens problem recursively.

    Args:
        board: A list of lists representing the chessboard.
        row: The current row.

    Returns:
        A list of all possible solutions to the N-queens problem.
    """

    if row == len(board):
        # We have reached the end of the board, so we have found a solution.
        return [board]

    solutions = []
    for col in range(len(board[0])):
        if is_valid_position(board, row, col):
            # Place a queen at the given position.
            board[row][col] = 1

            # Recursively solve the N-queens problem for the next row.
            new_solutions = solve_n_queens(board, row + 1)

            # Add the new solutions to the list of solutions.
            solutions += new_solutions

            # Remove the queen from the given position.
            board[row][col] = 0

    return solutions


def main():
    # Check if the user called the program with the wrong number of arguments.
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer.
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater or equal to 4.
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard.
    board = [[0 for i in range(n)] for j in range(n)]

    # Solve the N-queens problem.
    solutions = solve_n_queens(board, 0)

    # Print the solutions.
    for solution in solutions:
        print("".join(["Q" for i in range(len(solution)) if solution[i] == 1]))
