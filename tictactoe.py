"""tic-tac-toe.py

Author: XYLiu9357

Implementation of the tic-tac-toe game
"""

from enum import Enum, auto


class TicTacToe:
    """
    Static attributes:
    :PLAYER_O: indicates the player O
    :PLAYER_X: indicates the player X
    :class FillType(Enum): a class that has UNFILLED, FILLED_BY_O, and FILLED_BY_X, indicating the state of a slot

    Instance attributes:
    :int[] gameState: store the current state of the game in a 1*9 array using the state constants below
    :currentPlayer: the player that's currently playing, can be PLAYER_O or PLAYER_X
    :isOver: true if one of the player has won the game
    """

    # Players
    PLAYER_O = 1
    PLAYER_X = 2

    # FillType
    class __FillType(Enum):
        UNFILLED = 0
        FILLED_BY_O = auto()
        FILLED_BY_X = auto()

    # constructor
    def __init__(self) -> None:
        self.gameState = [TicTacToe.__FillType.UNFILLED] * 9
        self.currentPlayer = TicTacToe.PLAYER_X
        self.isOver = False

    # run
    def run(self) -> None:
        print("**Tic-tac-toe Game**")
        cmd = ""

        # Game keeps running
        while cmd != "$" and self.isOver == False:
            self.__printGrid()
            cmd = self.__newMove()
            if self.__isWin(TicTacToe.PLAYER_O) or self.__isWin(TicTacToe.PLAYER_X):
                self.isOver = True
                self.__printGrid()
            self.__updateCurrentPlayer()

        # Return name of the winner
        if self.isOver == False:
            winnerName = ""
            if self.currentPlayer == TicTacToe.PLAYER_O:
                winnerName = "player X"
            elif self.currentPlayer == TicTacToe.PLAYER_X:
                winnerName = "player O"

            print(f"The winner is {winnerName}!!!")

    # __printGrid
    def __printGrid(self) -> None:
        for pos in range(9):
            self.__printState(pos)

    # __printState
    # A helper function for __printGrid
    def __printState(self, pos) -> None:

        if pos == 0:
            print("-------------")

        match self.gameState[pos]:
            case TicTacToe.__FillType.UNFILLED:
                print(f"| {pos + 1}", end=" ")

            case TicTacToe.__FillType.FILLED_BY_O:
                print("| o", end=" ")

            case TicTacToe.__FillType.FILLED_BY_X:
                print("| x", end=" ")

            case _:
                print("**program encountered unexpected error in printing**")
                print("exit with code 1")
                exit(1)

        # End of row
        if (pos + 1) % 3 == 0:
            print("|\n-------------", end="\n")

    # __newMove
    def __newMove(self) -> str:

        # Prepare output message
        playerName = ""
        match self.currentPlayer:
            case TicTacToe.PLAYER_O:
                playerName = "O"

            case TicTacToe.PLAYER_X:
                playerName = "X"

        # Take user input
        cmd = input(
            "It's player "
            + playerName
            + "'s turn, input the number for an available slot, or input $ to stop the game > "
        )

        # Termination command
        if cmd == "$":
            print("**Terminating**")

        # Digit command
        elif str.isdigit(cmd):

            # A valid input must indicate a slot that's within range and is available
            if (
                1 <= int(cmd) <= 9
                and self.gameState[int(cmd) - 1] == TicTacToe.__FillType.UNFILLED
            ):
                # Save results
                self.__fillSlot(int(cmd))

            else:
                print(
                    "Please input a number in [1,9] that has not been occupied.\nYour number is out of range. "
                )

        else:
            print(
                "Command not found. Please input a number in [1,9] that has not been occupied"
            )

        return cmd

    # __updateCurrentPlayer
    def __updateCurrentPlayer(self) -> None:
        match self.currentPlayer:
            case TicTacToe.PLAYER_O:
                self.currentPlayer = TicTacToe.PLAYER_X

            case TicTacToe.PLAYER_X:
                self.currentPlayer = TicTacToe.PLAYER_O

    # __getFillType
    def __getFillType(self, player):
        match player:
            case TicTacToe.PLAYER_O:
                return TicTacToe.__FillType.FILLED_BY_O

            case TicTacToe.PLAYER_X:
                return TicTacToe.__FillType.FILLED_BY_X

    # __fillSlot
    # Given the slot #, fill the slot with the current player
    def __fillSlot(self, slot) -> None:
        # Prepare output message
        playerName = ""
        match self.currentPlayer:
            case TicTacToe.PLAYER_O:
                playerName = "O"

            case TicTacToe.PLAYER_X:
                playerName = "X"

        self.gameState[slot - 1] = self.__getFillType(self.currentPlayer)
        print("Player " + playerName + " has taken " + str(slot))

    def __isWin(self, player) -> bool:
        playerFillType = self.__getFillType(player)

        for i in range(3):
            # Win by row
            if (
                self.gameState[i * 3]
                == self.gameState[i * 3 + 1]
                == self.gameState[i * 3 + 2]
                == playerFillType
            ):
                return True

            # Win by column
            elif (
                self.gameState[i]
                == self.gameState[i + 3]
                == self.gameState[i + 6]
                == playerFillType
            ):
                return True

        # Win by diagonal
        if (
            self.gameState[0]
            == self.gameState[4]
            == self.gameState[8]
            == playerFillType
            or self.gameState[2]
            == self.gameState[4]
            == self.gameState[6]
            == playerFillType
        ):
            return True

        # No game-over condition is met
        return False
