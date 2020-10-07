"""

        BOARD - CLASS

"""


class Board(object):
    '''
    The Board defines contains :
    1. the list of Player nammed players -> list
    2. the list of active Card (the 6 last played card are active) nammed active_cards -> list each element: Card
    3. the list of played Card (should not contain the 6 last cards, those should be in the active list) nammed played_cards -> list

    '''

    def __init__(self, players: list, active_cards: list, played_cards: list):
        self.players = players
        self.active_cards = active_cards 
        self.played_cards = played_cards


