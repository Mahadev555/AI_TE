def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens_util(board, row, solutions):
    if row == len(board):
        solutions.append(board[:])  # Make a copy of the board
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1, solutions)
            board[row] = -1


def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, solutions)
    return solutions


# Test the code
n = 3
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-queens problem: {len(solutions)}")
for solution in solutions:
    for i in range(n):
        row = ['Q' if j == solution[i] else '.' for j in range(n)]
        print(' '.join(row))
    print()
