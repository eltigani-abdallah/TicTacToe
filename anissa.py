import random

class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        """Create a 3x3 empty board."""
        for i in range(3):
            row = ['-' for _ in range(3)]
            self.board.append(row)

    def get_random_first_player(self):
        """Randomly choose who goes first: 'X' or 'O'."""
        return random.choice(['X', 'O'])

    def fix_spot(self, row, col, player):
        """Place a player's mark ('X' or 'O') on the board."""
        self.board[row][col] = player

    def is_player_win(self, player):
        """Check if a player has won the game."""
        n = len(self.board)

        # Check rows
        for i in range(n):
            if all(self.board[i][j] == player for j in range(n)):
                return True

        # Check columns
        for i in range(n):
            if all(self.board[j][i] == player for j in range(n)):
                return True

        # Check diagonal (top-left to bottom-right)
        if all(self.board[i][i] == player for i in range(n)):
            return True

        # Check diagonal (top-right to bottom-left)
        if all(self.board[i][n - 1 - i] == player for i in range(n)):
            return True

        return False

    def is_board_filled(self):
        """Check if the board is filled (no empty spots)."""
        for row in self.board:
            if '-' in row:
                return False
        return True

    def swap_player_turn(self, current_player):
        """Switch turns between 'X' and 'O'."""
        return 'X' if current_player == 'O' else 'O'

    def show_board(self):
        """Display the current state of the board."""
        for row in self.board:
            print(" ".join(row))

    def start(self):
        """Start the Tic-Tac-Toe game."""
        self.create_board()

        player = self.get_random_first_player()
        while True:
            print(f"\nIt's {player}'s turn.")
            self.show_board()

            # Get user input for row and column
            try:
                row, col = map(int, input("Enter row and column (1-3) to place your mark: ").split())
                row, col = row - 1, col - 1  # Adjust for 0-based index
                if self.board[row][col] != '-':
                    print("That spot is already taken! Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers between 1 and 3.")
                continue

            # Place the player's mark on the board
            self.fix_spot(row, col, player)

            # Check if the player has won
            if self.is_player_win(player):
                self.show_board()
                print(f"\nPlayer {player} wins!")
                break

            # Check if the board is filled (draw)
            if self.is_board_filled():
                self.show_board()
                print("It's a draw!")
                break

            # Switch players
            player = self.swap_player_turn(player)


# Start the game
if __name__ == "__main__":
    game = TicTacToe()
    game.start()
