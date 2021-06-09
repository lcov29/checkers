from source.Checkers import Checkers
from source.Observer import Observer
from source.AdapterPrint import AdapterPrint


class TerminalGame:

    __checkers = None

    def __init__(self, difficulty):
        self.__checkers = Checkers(difficulty)
        observer = Observer(self, AdapterPrint())
        self.__checkers.add_observer(observer)


    def print_board(self):
        self.__checkers.send_external_board()


    def show_moves_for(self, row, column):
        self.__checkers.get_possible_moves_for(row, column)


    def execute_move_for(self, row, column):
        self.__checkers.execute_move(row, column)


    def get_winner(self):
        return self.__checkers.get_winner()


    # Callback-methods
    def draw_board(self, board):
        print(board)


    def show_possible_moves(self, moves):
        print(moves)




game = TerminalGame(4)

print("-- Welcome to Chekcers --\n")

while True:
    command = input("(n) new game or (q) quit : ")
    if command == "n":
        game = TerminalGame(4)
        game.print_board()

        while True:
            command_2 = input("(s) select queen, (q) quit game: ")
            if command_2 == "q":
                break
            elif command_2 == "s":
                print("\n\tSelect a queen")
                queen_row = int(input("\t\trow: "))
                queen_column = int(input("\t\tcolumn: "))
                game.show_moves_for(queen_row, queen_column)
                while True:
                    command_3 = input("\n(m) move selected queen, (u) unselect queen: ")
                    if command_3 == "u":
                        break
                    elif command_3 == "m":
                        queen_row = int(input("\t\tmove to row: "))
                        queen_column = int(input("\t\tmove to column: "))
                        game.execute_move_for(queen_row, queen_column)
                        break
                    else:
                        print("Unknown command")
            else:
                print("Unknown command")

            game.print_board()
            winner = game.get_winner()
            if winner != "":
                print(str(winner) + " wins")
                quit()

    elif command == "q":
        print("Bye.")
        break
    else:
        print("unknown command")
