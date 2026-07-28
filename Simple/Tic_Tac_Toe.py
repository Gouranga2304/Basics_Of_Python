def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(" | ".join(row))
        if i < 6:
            print("--+---+--")
    print()


def check_winner(board):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]

    for combo in win_combinations:
        a, b, c = combo
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]  # returns 'X' or 'O'

    return None


def is_board_full(board):
    return " " not in board


def get_valid_move(board, player):
    while True:
        move = input(f"Player {player}, enter position (1-9): ").strip()

        if not move.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        move = int(move) - 1

        if move < 0 or move > 8:
            print("Please enter a number between 1 and 9.")
            continue

        if board[move] != " ":
            print("That position is already taken. Try again.")
            continue

        return move


def play_game():
    board = [" "] * 9
    current_player = "X"

    print("=== Tic-Tac-Toe ===")
    print("Positions are numbered 1-9 like this:")
    print_board([str(i) for i in range(1, 10)])

    while True:
        print_board(board)
        move = get_valid_move(board, current_player)
        board[move] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()