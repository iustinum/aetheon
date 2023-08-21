# Codebase Overview

The codebase consists of three main files: **deck.py**, **game.py**, and **main.py**. These files contain the implementation of a card game, specifically a poker game, as well as a Discord bot representation of the game.

## deck.py

The **deck.py** file contains the implementation of the card game's deck. It defines three classes: `Card`, `Deck`, and `Player`.

### Card Class
The `Card` class represents a single playing card. It has the following variables:
- `suit`: Represents the suit of the card (e.g., "Spades", "Hearts", "Diamonds", "Clubs").
- `number`: Represents the number or face value of the card (e.g., "Ace", 2, 3, ..., 10, "Jack", "Queen", "King").
- `default_value`: Represents the default value of the card (optional). If not provided, it defaults to the `number` value.

The `Card` class provides the following functions:
- `__init__(self, suit, number, default_value=None)`: Initializes a `Card` object with the given suit, number, and default value.
- `__repr__(self)`: Returns a string representation of the card in the format "suit-number".

### Deck Class
The `Deck` class represents a deck of cards. It has the following variables:
- `allcards`: A list of `Card` objects representing all the cards in the deck.
- `cards`: A list of `Card` objects representing the current cards in the deck.
- `num_cards`: Represents the number of cards remaining in the deck.

The `Deck` class provides the following functions:
- `__init__(self)`: Initializes a `Deck` object by copying all the cards from `allcards` to `cards` and setting `num_cards` to 52.
- `draw(self, amount)`: Draws the specified number of cards from the deck and returns them as a list of `Card` objects.

### Player Class
The `Player` class represents a player in the card game. It has the following variables:
- `name`: Represents the name of the player.
- `hand`: A list of `Card` objects representing the player's current hand.
- `total_money`: Represents the total amount of money the player has.
- `round_result`: Represents the result of the player's current round (optional).
- `money_betted`: Represents the amount of money the player has betted in the current round.

The `Player` class provides the following functions:
- `__init__(self, name, total_money=1000)`: Initializes a `Player` object with the given name and total money.
- `__repr__(self)`: Returns a string representation of the player's name.
- `draw(self, deck)`: Draws two cards from the deck and adds them to the player's hand.

### PlayerDiscordVer Class
The `PlayerDiscordVer` class is a subclass of the `Player` class and represents a player associated with a Discord user. It adds an additional variable `user` representing the Discord user. This class overrides the `draw` function to call the parent class's `draw` function.

## game.py

The **game.py** file contains the implementation of the poker game. It defines a `Game` class, representing a game of poker. The class has several variables and functions.

### Game Class
The `Game` class represents a game of poker. It has the following variables:
- `deck`: An instance of the `Deck` class, representing the deck of cards used in the game.
- `players`: A list that stores instances of the `PlayerDiscordVer` class, representing the players in the game.
- `displayhand`: A list that stores the cards drawn from the deck to be displayed during the game.
- `pot`: An integer representing the total amount of money betted by the players.
- `current_bet`: An integer representing the current highest bet in the game.
- `players_in_game`: A list that stores instances of the `PlayerDiscordVer` class, representing the players who are still in the game.

The `Game` class provides the following functions:
- `__init__(self)`: The constructor method that initializes the `Game` object. It initializes the variables deck, players, displayhand, pot, current_bet, and players_in_game.
- `add_player(self, *args)`: A method that adds player instances to the game's player list. It takes in one or more arguments of type `PlayerDiscordVer` and adds them to the players and players_in_game lists.
- `give_hand_to_each_player(self)`: A method that gives two cards to each player in the game. It calls the `draw` method of each player to draw cards from the deck.
- `draw_one(self)`: A method that draws one card from the deck and adds it to the displayhand list.
- `start_round(self)`: A method that starts a round of the game. It gives two cards to each player, adds 10 to each player's `money_betted`, draws three cards to the displayhand, asks each player for their action, assigns the round result, and declares the winner.
- `ask_player(self, raise_player=None)`: A method that asks each player for their action in the game. It takes an optional argument `raise_player`, which represents the player who raised the bet. It loops through the players_in_game list and asks each player if they want to raise, match, or fold the current bet amount.

## main.py

The **main.py** file serves as the main entry point for the PokerBot application. It contains several variables and functions that are used to implement the functionality of the bot.

### Variables
- `TOKEN`: This variable stores the Discord bot token, which is used to authenticate the bot with the Discord API.
- `bot`: This variable represents an instance of the `discord.ext.commands.Bot` class, which is used to define and handle bot commands.
- `game`: This variable represents an instance of the `GameDiscordVer` class, which is responsible for managing the game state and players.

### Functions
- `on_ready()`: This function is an event handler that is called when the bot is successfully connected to the Discord server. It simply prints a message to indicate that the bot is online.
- `test(ctx)`: This function is a command handler that is triggered when the "&test" command is invoked. It sends a message to the channel and waits for a response from the same user in the same channel. If the response is "yes", it invokes the "test2" command. Otherwise, it sends a "No" message.
- `test2(ctx)`: This function is a command handler that is triggered when the "&test2" command is invoked. It sends a message to the channel and waits for a response from the same user in the same channel. After receiving the response, it sends an "okay" message.
- `test3(ctx)`: This function is a command handler that is triggered when the "&test3" command is invoked. It sends a message to the channel and waits for a response from the same user in the same channel. After receiving the response, it adds 3 to the number and sends the result back to the channel.
- `join(ctx, user)`: This function is a command handler that is triggered when the "&join" command is invoked with a user mention as an argument. It creates a `PlayerDiscordVer` object for the mentioned user and adds it to the game. It sends a message to the channel to indicate that the user has joined the game.
- `give_hand(ctx)`: This function is a command handler that is triggered when the "&give_hand" command is invoked. It iterates over the players in the game and sends each player a private message with their hand.
- `start(ctx)`: This function is a command handler that is triggered when the "&start" command is invoked. It invokes the "give_hand" command, sets the initial bet amount, and draws three cards for the game. It sends a message to the channel to display the current hand and the current highest bet.

The main.py file defines the main functionality of the PokerBot application, including handling commands, managing game state, and interacting with the Discord API.

*Please note that this is a high-level overview of the codebase and additional details, such as the implementation of individual functions, may not be provided.*
