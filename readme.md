## CARD GAME 


### [1. Description]
    Card game is a small game with **no winnig logic**
    The game starts by asking the user to enter the number of players and their names.
    Each player will receive 10 card random cards.
    Every round each player put one card on the board. 

    Finally the game ends when all players have no more card on theirs hands. 

    The game starts by running main.py.
    

### [2. File Structure]

    In order to make it clear I have choose to put each classes in a single file.

    There is two module that imports other module:
    1. **main** imports board, player, game
    2. **game** imports card

    

    .
├── __pycache__
│   
├── main.py
├── readme.md
└── utils
    ├── __pycache__
    │  
    ├── board.py
    ├── card.py
    ├── game.py
    └── player.py

### [3. Cards]
    # Card class containing:

        ## A color -> string
        ## A number -> int
        ## A symbol -> string Symbols are: [♥, ♦, ♣, ♠]


### [4. Board]
    Create a Board class containing:

    A list of Player nammed players -> list
    
    # For Each Player, board holds:
        ## a list of active Card (the 6 last played card are active) nammed active_cards -> list
        ## a list of played Card (should not contain the 6 last cards, those should be in the active list) nammed played_cards -> list


### [5. Player]
    # Player contains:

    ## A name nammed name
    ## A list of Card (each player start with 10 Card) 
    ## A play() method that throw a Card in the Board
    ## A shuffle() method that shuffle all the Card of the player.