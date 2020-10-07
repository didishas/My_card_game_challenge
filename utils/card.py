
"""

        CARD - CLASS

"""

class Card(object):
    '''
    The Class defines the specification of the card, it should have:
    1. a color -> string
    2. a number -> int
    3. a symbol -> string [♥, ♦, ♣, ♠]

    '''

    card_sets: dict = {
        'red': ['♥', '♦'],
        'back': ['♣', '♠']
    }

    # these are the possible values that a card may have
    values: str = ['A','2','3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, color: str, number: int, symbol: str) :
        self.color = color
        self.symbol = symbol
        

