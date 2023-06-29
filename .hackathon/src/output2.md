# PokerBot Codebase

PokerBot is a Discord bot that facilitates playing poker with friends through Discord text channels. The codebase is divided into multiple files, each containing different classes, functions, and variables responsible for managing the game.

## main.py

Main file containing the Discord bot implementation.

### Variables

- TOKEN: The Discord bot token
- bot: Instance of the Discord `commands.Bot` class
- game: Instance of the `GameDiscordVer` class
- player: Instance of the `PlayerDiscordVer` class
- check: Function to check if the message is from the author and in the correct channel
- msg: A message object
- raise_user: A user object
- winner: A player object
- hand_name: A string containing the name of the winning hand

### Functions

#### on_ready()

Prints "Poker Bot Online" when the bot is ready.

#### test()

Sends a message to the user and invokes the `test2` command if the user responds with "yes".

#### test2()

Sends a message to the user.

#### test3()

Sends a message to the user and adds 3 to the number they respond with.

#### join()

Adds a user to the game.

#### give_hand()

Sends each player their hand.

#### start()

Invokes the `give_hand` command, adds 10 to each player's money betted, draws one card, invokes the `ask_player` command, assigns the round result, and invokes the `declare_winner` command.

#### ask_player()

Sends a message to the player asking how much they would like to raise the current amount to.

#### declare_winner()

Sorts the players in the game by their round result, declares the winner, invokes the `add_pot_to_winner` command, and invokes the `reset` command.

#### add_pot_to_winner()

Adds the pot to the winner's total money.

#### reset()

Resets the game.

#### in_game()

Sends the number of players in the game.

#### DM()

Sends a direct message to a user.

## deck.py

Contains the `Card`, `Deck`, and `PlayerDiscordVer` classes.

### Card class

#### Variables

- suit: The card's suit
- number: The card's number
- default_value: The card's default value

#### Functions

##### __repr__()

Returns a string representation of the card.

### Deck class

#### Variables

- allcards: A list of `Card` objects

#### Functions

##### __init__()

Initializes the deck.

##### draw()

Draws a specified number of cards from the deck.

### PlayerDiscordVer class

A subclass of `Player`.

#### Variables

- user: The Discord user
- hand: The player's hand
- total_money: The player's total money
- round_result: The player's round result
- money_betted: The player's money betted
- responded: Whether the player has responded

#### Functions

##### draw()

Draws two cards from the deck for the player.

## game.py

Contains the `Game` class, which is used to manage the game of poker.

### Variables

- deck: A `Deck` object containing the cards used in the game
- players_in_game: A list of `Player` objects currently in the game
- current_bet: The current highest bet in the game
- displayhand: A list of the cards currently in play

### Functions

#### add_player(player)

Adds a `Player` object to the `players_in_game` list.

#### draw_one()

Draws one card from the deck and adds it to the `displayhand` list.

#### assign_round_result()

Assigns a result to the round based on the cards in the `displayhand` list.

#### declare_winner()

Declares the winner of the round based on the result assigned by the `assign_round_result()` function.

## README.md

A text file that provides an overview of the PokerBot and the commands it supports. It does not contain any variables or functions.