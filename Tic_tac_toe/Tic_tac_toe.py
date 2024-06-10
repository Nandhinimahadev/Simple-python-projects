from tkinter import *
import numpy as np
import random

sizeOfBoard = 700
symbolSize = (sizeOfBoard / 3 - sizeOfBoard / 8) / 2
symbolThickness = 50
symbolXColor = "#005f73"
symbolOColor = "#ca6702"
Color = "#b8001f"


class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.canvas = Canvas(self.window, width=sizeOfBoard, height=sizeOfBoard)
        self.canvas.pack()
        self.window.bind("<Button-1>", self.click)

        self.initialize_board()
        self.playerXTurns = True
        self.boardStatus = np.zeros(shape=(3, 3))

        self.playerXStarts = True
        self.resetBoard = False

        self.XScore = 0
        self.OScore = 0
        self.tieScore = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line(
                (i + 1) * sizeOfBoard / 3,
                0,
                (i + 1) * sizeOfBoard / 3,
                sizeOfBoard,
            )

        for i in range(2):
            self.canvas.create_line(
                0,
                (i + 1) * sizeOfBoard / 3,
                sizeOfBoard,
                (i + 1) * sizeOfBoard / 3,
            )

    def play_again(self):
        self.canvas.delete("all")
        self.initialize_board()
        self.playerXStarts = not self.playerXStarts
        self.playerXTurns = self.playerXStarts
        self.boardStatus = np.zeros(shape=(3, 3))
        self.resetBoard = False

    def draw_O(self, logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(
            grid_position[0] - symbolSize,
            grid_position[1] - symbolSize,
            grid_position[0] + symbolSize,
            grid_position[1] + symbolSize,
            width=symbolThickness,
            outline=symbolOColor,
        )

    def draw_X(self, logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(
            grid_position[0] - symbolSize,
            grid_position[1] - symbolSize,
            grid_position[0] + symbolSize,
            grid_position[1] + symbolSize,
            width=symbolThickness,
            fill=symbolXColor,
        )
        self.canvas.create_line(
            grid_position[0] - symbolSize,
            grid_position[1] + symbolSize,
            grid_position[0] + symbolSize,
            grid_position[1] - symbolSize,
            width=symbolThickness,
            fill=symbolXColor,
        )

    def display_gameover(self):
        if self.X_wins:
            self.XScore += 1
            text = "Winner: User (X)"
            color = symbolXColor
        elif self.O_wins:
            self.OScore += 1
            text = "Winner: Computer (O)"
            color = symbolOColor
        else:
            self.tieScore += 1
            text = "It's a tie"
            color = "gray"

        self.canvas.delete("all")
        self.canvas.create_text(
            sizeOfBoard / 2,
            sizeOfBoard / 3,
            font="cmr 60 bold",
            fill=color,
            text=text,
        )

        score_text = "Scores \n"
        self.canvas.create_text(
            sizeOfBoard / 2,
            5 * sizeOfBoard / 8,
            font="cmr 20 bold",
            fill=Color,
            text=score_text,
        )

        score_text = "User (X) : " + str(self.XScore) + "\n"
        score_text += "Computer (O): " + str(self.OScore) + "\n"
        score_text += "Tie               : " + str(self.tieScore)
        self.canvas.create_text(
            sizeOfBoard / 2,
            3 * sizeOfBoard / 4,
            font="cmr 30 bold",
            fill=Color,
            text=score_text,
        )
        self.resetBoard = True

        score_text = "Click to play again \n"
        self.canvas.create_text(
            sizeOfBoard / 2,
            15 * sizeOfBoard / 16,
            font="cmr 20 bold",
            fill="gray",
            text=score_text,
        )

    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (sizeOfBoard / 3) * logical_position + sizeOfBoard / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (sizeOfBoard / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        if self.boardStatus[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    def is_winner(self, player):
        player = -1 if player == "X" else 1

        for i in range(3):
            if (
                self.boardStatus[i][0]
                == self.boardStatus[i][1]
                == self.boardStatus[i][2]
                == player
            ):
                return True
            if (
                self.boardStatus[0][i]
                == self.boardStatus[1][i]
                == self.boardStatus[2][i]
                == player
            ):
                return True

        if (
            self.boardStatus[0][0]
            == self.boardStatus[1][1]
            == self.boardStatus[2][2]
            == player
        ):
            return True

        if (
            self.boardStatus[0][2]
            == self.boardStatus[1][1]
            == self.boardStatus[2][0]
            == player
        ):
            return True

        return False

    def is_tie(self):
        r, c = np.where(self.boardStatus == 0)
        tie = False
        if len(r) == 0:
            tie = True

        return tie

    def is_gameover(self):
        self.X_wins = self.is_winner("X")
        if not self.X_wins:
            self.O_wins = self.is_winner("O")

        if not self.O_wins:
            self.tie = self.is_tie()

        gameover = self.X_wins or self.O_wins or self.tie

        if self.X_wins:
            print("User wins")
        if self.O_wins:
            print("Computer wins")
        if self.tie:
            print("It's a tie")

        return gameover

    def random_move(self):
        empty_cells = np.argwhere(self.boardStatus == 0)
        if len(empty_cells) > 0:
            move = random.choice(empty_cells)
            self.draw_O(move)
            self.boardStatus[move[0]][move[1]] = 1
            self.playerXTurns = not self.playerXTurns

    def click(self, event):
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if not self.resetBoard:
            if self.playerXTurns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.boardStatus[logical_position[0]][logical_position[1]] = -1
                    self.playerXTurns = not self.playerXTurns
                    if self.is_gameover():
                        self.display_gameover()
                    else:
                        self.random_move()
                        if self.is_gameover():
                            self.display_gameover()
            else:
                pass
        else:
            self.play_again()
            self.resetBoard = False


game_instance = TicTacToe()
game_instance.mainloop()
