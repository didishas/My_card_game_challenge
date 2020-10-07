import time

from utils.game import Game
from utils.player import Player
from utils.board import Board

list_of_players = []

def play():

    '''
        GAME
        Generating and Suffling cards for the game
    '''
    # 1.  initialise the game and create all cards which will be used in the game
    game = Game()
    all_cards = game.card_list

    # 2. Suffling the cards before distributing
    game.suffle_card_game(all_cards)

    # 3. numbers of players for that game
    number_players = 0
    # condition for max number of player ( as we have 52 cards we can not have than 5 players, total card we be 50)
    while number_players == 0 or number_players > 5:
        number_players_string = input('how much players needs to play : ')
        number_players = int(number_players_string)

    
    ''' 
        PLAYER
        Initialisation and instanciation of players( name, card)
    '''

    for i in range(number_players):
        name_of_player = input(f"Enter name Player {i}: ")

        # instanciate Player with the 10 first cards
        player = Player(name_of_player, all_cards[:10])
        print(player.cards)
        # removing those cards from the all cards set to avoid repetitions
        all_cards = all_cards[10:]
        # append the player to a list of player
        list_of_players.append(player)

    """
        BOARD
        instanciate the Board for the all game

    """
        
    board = Board(list_of_players,[],[])

    #Setting up the active and played card for each player
    for i in range(number_players):
        board.active_cards.append([])
        board.played_cards.append([])


    """
        lOOP - FOR 
        10 Times for each player
        6 first times the list of active_card got append by previous card
        after the 6th oldest got in played_card list
    """

    for i in range(10):

        for player in list_of_players:
            player_indice = list_of_players.index(player)

            board.active_cards[player_indice].append(player.play())
            time.sleep(1.5)

            # When the active list will reach len of 6, old card played will be pushed in card_played list

            if len(board.active_cards[player_indice]) > 6:
                board.played_cards[player_indice].append(board.active_cards[player_indice][0])
                del board.active_cards[player_indice][0]

                print( """ Name: {}
                active cards: {}
                played cards: {}
                """.format(player.name, board.active_cards[player_indice], board.played_cards[player_indice]))
            else:
                print( """ Name: {}
                active cards: {}
                """.format(player.name, board.active_cards[player_indice]))
            
play()


print("hello")

    


