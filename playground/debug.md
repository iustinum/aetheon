# Important Functions

## Class: Card

### __init__(self, suit, number, default_value=None)

**Description:**
This function initializes a `Card` object with the given suit, number, and default value. It sets the `suit` and `number` instance variables to the provided values, and if a `default_value` is provided, it sets the `default_value` instance variable to that value; otherwise, it defaults to the `number` value.

**Arguments:**
- `suit` (string): Represents the suit of the card (e.g., "Spades", "Hearts", "Diamonds", "Clubs").
- `number` (string or integer): Represents the number or face value of the card (e.g., "Ace", 2, 3, ..., 10, "Jack", "Queen", "King").
- `default_value` (optional): Represents the default value of the card. If not provided, it defaults to the `number` value.

**Return Value:**
None

**Side Effects:**
None

### __repr__(self)

**Description:**
This function returns a string representation of the card in the format "suit-number".

**Arguments:**
None

**Return Value:**
string: A string representation of the card in the format "suit-number".

**Side Effects:**
None

## Class: Deck

### __init__(self)

**Description:**
This function initializes a `Deck` object by copying all the cards from the `allcards` variable to the `cards` variable and setting `num_cards` to 52.

**Arguments:**
None

**Return Value:**
None

**Side Effects:**
- Initializes the `cards` variable by copying all the cards from the `allcards` variable.
- Sets the `num_cards` variable to 52.

### draw(self, amount)

**Description:**
This function draws the specified number of cards from the deck and returns them as a list of `Card` objects. It removes the drawn cards from the `cards` list.

**Arguments:**
- `amount` (integer): The number of cards to draw from the deck.

**Return Value:**
list of `Card` objects: The drawn cards as a list of `Card` objects.

**Side Effects:**
- Removes the drawn cards from the `cards` list.

## Class: Player

### __init__(self, name, total_money=1000)

**Description:**
This function initializes a `Player` object with the given name and total money. It sets the `name` and `total_money` instance variables to the provided values, and initializes the `hand`, `round_result`, and `money_betted` instance variables.

**Arguments:**
- `name` (string): Represents the name of the player.
- `total_money` (optional, integer): Represents the total amount of money the player has. Defaults to 1000 if not provided.

**Return Value:**
None

**Side Effects:**
- Initializes the `hand`, `round_result`, and `money_betted` instance variables.

### __repr__(self)

**Description:**
This function returns a string representation of the player's name.

**Arguments:**
None

**Return Value:**
string: A string representation of the player's name.

**Side Effects:**
None

### draw(self, deck)

**Description:**
This function draws two cards from the deck and adds them to the player's hand. It uses the `draw` function of the `Deck` class.

**Arguments:**
- `deck` (object): An instance of the `Deck` class representing the deck of cards.

**Return Value:**
None

**Side Effects:**
- Adds two cards to the player's hand.

## Class: PlayerDiscordVer

### draw(self, deck)

**Description:**
This function overrides the `draw` function of the `Player` class and calls the parent class's `draw` function. It draws two cards from the deck and adds them to the player's hand.

**Arguments:**
- `deck` (object): An instance of the `Deck` class representing the deck of cards.

**Return Value:**
None

**Side Effects:**
- Adds two cards to the player's hand.

## Class: Game

### __init__(self)

**Description:**
This function initializes the `Game` class. It initializes the variables `deck`, `players`, `displayhand`, `pot`, `current_bet`, and `players_in_game`. It creates an instance of the `Deck` class for the `deck` variable.

**Arguments:**
None

**Return Value:**
None

**Side Effects:**
- Initializes the `deck` variable with an instance of the `Deck` class.
- Initializes the variables `players`, `displayhand`, `pot`, `current_bet`, and `players_in_game`.

### add_player(self, *args)

**Description:**
This function adds player instances to the game's player list. It takes in one or more arguments of type `PlayerDiscordVer` and adds them to the `players` and `players_in_game` lists.

**Arguments:**
- `*args` (PlayerDiscordVer): One or more instances of the `PlayerDiscordVer` class representing the players to be added.

**Return Value:**
None

**Side Effects:**
- Adds player instances to the `players` and `players_in_game` lists.

### give_hand_to_each_player(self)

**Description:**
This function gives two cards to each player in the game by calling the `draw` method of each player to draw cards from the deck.

**Arguments:**
None

**Return Value:**
None

**Side Effects:**
- Adds two cards to each player's hand.

### draw_one(self)

**Description:**
This function draws one card from the deck and adds it to the `displayhand` list.

**Arguments:**
None

**Return Value:**
None

**Side Effects:**
- Adds one card to the `displayhand` list.

### start_round(self)

**Description:**
This function starts a round of the game. It gives two cards to each player, adds 10 to each player's `money_betted`, draws three cards to the `displayhand`, asks each player for their action, assigns the round result, and declares the winner.

**Arguments:**
None

**Return Value:**
None

**Side Effects:**
- Gives two cards to each player.
- Adds 10 to each player's `money_betted`.
- Draws three cards to the `displayhand`.
- Asks each player for their action.
- Assigns the round result.
- Declares the winner.

### ask_player(self, raise_player=None)

**Description:**
This function asks each player for their action in the game. It takes an optional argument `raise_player`, which represents the player who raised the bet. It loops through the `players_in_game` list and asks each player if they want to raise, match, or fold the current bet amount.

**Arguments:**
- `raise_player` (optional, PlayerDiscordVer): Represents the player who raised the bet.

**Return Value:**
None

**Side Effects:**
- Asks each player for their action.
