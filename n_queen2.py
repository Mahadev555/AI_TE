def is_safe(board, row, col):
    # Check if the current position is safe for a queen

    # Check the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]  # Initialize an empty chessboard

    if not solve_n_queens_util(board, 0):
        print("No solution found.")
        return False

    print_board(board)
    return True


def solve_n_queens_util(board, col):
    # Base case: All queens have been placed
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen in the current position
            board[i][col] = 1

            # Recur to place the remaining queens
            if solve_n_queens_util(board, col + 1):
                return True

            # Backtrack and remove the queen from the current position
            board[i][col] = 0

    return False


def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))


# Example usage
n = 4 # Number of queens
solve_n_queens(n)
