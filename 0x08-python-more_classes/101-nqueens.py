import sys


def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or board[i] - i == row - col:
            return False
        if board[i] + i == row + col:
            return False
    return True


def solve_n_queens(board, col, n):
    if col == n:
        print(board)
        return
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve_n_queens(board, col + 1, n)
            board[col] = -1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solve_n_queens(board, 0, n)
