# PokerBot Codebase

The PokerBot codebase is designed for creating, managing, and operating a Discord-based poker game. It contains several Python files, each serving a different purpose in the functioning of the bot and game management.

## README.md

README.md is a text file that provides an overview of the PokerBot and the available commands. It does not contain any variables or functions.

## deck.py

deck.py is a Python file that contains the following classes and subclass:

### Card class

The `Card` class has the following variables:
- `suit`
- `number`
- `default_value`

This class also has a function called `__repr__`, which returns a string representation of the card.

### Deck class

The `Deck` class contains the following variable:
- `allcards`: A list of Card objects

It also has the following functions:
- `__init__`: Initializes the deck
- `draw`: Draws a specified number of cards from the deck

### PlayerDiscordVer subclass

The `PlayerDiscordVer` subclass contains the following variables:
- `user`
- `hand`
- `total_money`
- `round_result`
- `money_betted`
- `responded`

This subclass has a function called `draw`, which draws two cards from the deck.

## game.py

game.py is a Python file containing the `Game` class, used for managing the poker game. The class includes the following variables:

- `deck`: A Deck object containing the game's cards
- `players_in_game`: A list of Player objects currently in the game
- `current_bet`: The current highest bet in the game
- `displayhand`: A list of the cards currently in play

The `Game` class also contains the following functions:

### add_player()

This function adds a `Player` object to the `players_in_game` list.

### draw_one()

This function draws one card from the deck and adds it to the `displayhand` list.

### assign_round_result()

This function assigns a result to the round based on the cards in the `displayhand` list.

### declare_winner()

This function declares the winner of the round based on the result assigned by the `assign_round_result()` function.

## main.py

main.py is a Python file that contains code for a Discord bot, importing the string, discord, and game modules, as well as the Deck class from the deck module. It also defines a `TOKEN` variable for bot authentication.

The file contains a `BoThe file contains a `Bot` object for interacting with the Discord API, and a `GameDiscordVer` object for managing the game. It includes several functions:
t` object for interacting with the Discord API, and a `GameDiscordVer` object for managing the game. It includes several functions:

### on_ready()

This function is called when the bot is ready to start and prints a message to the console.

### test()

This function tests functions, sends a message to the user, and waits for a response. If the response is "yes", it invokes the `test2()` function. Otherwise, it sends a "No" message.

### test2()

This function sends a message to the user asking if they are sure.

### test3()

This function sends a message to the user asking them to reply with a number. It then adds 3 to the number and sends the result back to the user.

### join()

This function adds a user to the game, creates a `PlayerDiscordVer` object for the user, and adds the player to the game.

### give_hand()

This function gives each player in the game a hand by drawing a card for each player and sending a message with their hand.

### start()

This function starts the game, invoking the `give_hand()` function and adding 10 to the money betted for each player. It then draws three cards and sends a message with the current hand and highest bet. It invokes the `ask_player()` function and the `declare_winner()` function.

### ask_player()

This function asks each player in the game to either raise or fold, taking an optional argument, `raise_user`, specifying which player should raise.

### declare_winner()

This function declares the winner of the round, assigning the round result and sending a message with the winner to the channel.