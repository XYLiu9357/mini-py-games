# Mini-Python-Games

This repository contains a collection of mini games implemented in Python. All the games have a `run()` method, and the appropriate way to access and run the games would be to create a game object that matches the type of game. Some games may have one or more bot-opponents. Checkout the documentation for each individual game below. Have fun! 

## Tic-tac-toe 

This project aims to implement the game tic-tac-toe in python. A 3x3 grid will be generated in the terminal. Two players can enter "o" or "x" and the rest of the rules are exactly the same as the traditional game: whoever gets three consecutive slots (whether it's horizontal, vertical, or diagonal), wins the game. 

### Run 

Import from `ticatactoe` module the game class. 
```
from tictactoe import TicTacToe
```

Create a game object and call the run method. 
```
tic_tac_toe = TicTacToe()
winner = tic_tac_toe.run()
```
Done! 

### Game Logic 

1. **Create a grid** that looks like "|  |  |" repeated three times. 
2. **Repeatedly take user inputs**. Two spaces between each of the vertical bars, and the user could enter their symbol between the spaces, like "| o | o | x |". Note that this process can go on forever. Don't add the check-win mechanism until the end. 
3. **Keep user inputs**. Once enter is pressed, the entered character becomes part of the game's structure, i.e. changes are permanent until the end. 
4. **Check wins after every input**. Every time a player enters a symbol, it might be the case that this player wins. The program checks if any of the player has won this game. 

### Future Updates 
- A GUI will be added to the mini-game 
- A tic-tac-toe bot will be added to the mini-game and callable in `main` with `run(bot=True)`. 
